"""
routes that provide read-only access to xyz_trade db
"""
from app import app, db
from app.models import Account, Transactions
from flask import request, abort, jsonify
from werkzeug.security import check_password_hash


@app.route('/api/v1/login', methods=['GET'])
def login():
    """
    return 200 if credentials are valid, 401 otherwise
    """
    account_login = request.args.get("account_login")
    account_password = request.args.get("account_password")

    account = Account.query.filter_by(account_login=account_login).first()

    if account is None:
        # invalid login
        abort(400)

    if not check_password_hash(account.account_password_hash, account_password):
        # invalid password
        abort(401)

    password_hash = account.account_password_hash
    return jsonify({"account_login": account_login, "account_password_hash": password_hash}), 200


@app.route('/api/v1/account', methods=['GET'])
def get_account():
    """
    return the account balance
    """
    account_login = request.args.get("account_login")
    account_password_hash = request.args.get("account_password_hash")
    account = Account.query.filter_by(account_login=account_login,
            account_password_hash=account_password_hash).first()

    if account is None:
        abort(400)

    return jsonify({"id": account.id, "balance": account.account_balance}), 200


@app.route('/api/v1/transactions', methods=['GET'])
def get_transactions():
    """
    return the transactions for an account
    """
    account_id = request.args.get("account_id")
    transactions = Transactions.query.filter_by(account_id=account_id).all()

    return jsonify(json_list=[{"date": i.transaction_date,
        "seller": i.transaction_seller,
        "amount": i.transaction_amount,
        "id": i.id} for i in transactions]), 200
