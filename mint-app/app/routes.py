from app import app, db

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from flask import request, abort, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Account, Transaction, institutions, categories, Spending
from app.forms import LoginForm, RegistrationForm, AccountForm, CategoryForm
from collections import OrderedDict
import redis
import json
from datetime import datetime
import hashlib
import requests


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        accounts = Account.query.filter_by(user_id=current_user.id)
        total_balance = 0
        for account in accounts:
            total_balance += account.account_balance
        return render_template('index.html', total_balance=total_balance)

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not check_password_hash(user.password_hash, form.password.data):
            flash('Invalid username or password')
            return

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not check_password_hash(user.password_hash, form.password.data):
            flash('Invalid username or password')
            return

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.password_hash = generate_password_hash(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


def calculate_spending(transactions):
    spending_dict = {}
    month_spending_dict = {}
    for transaction in transactions:
        trans_date = transaction.transaction_date.strftime("%Y-%m")
        trans_amount = transaction.transaction_amount
        category = transaction.category
        key = (trans_date, category)
        if key not in spending_dict:
            spending_dict[key] = trans_amount
        else:
            spending_dict[key] = spending_dict[key] + trans_amount
        month_key = trans_date
        if month_key not in month_spending_dict:
            month_spending_dict[month_key] = trans_amount
        else:
            month_spending_dict[month_key] = month_spending_dict[month_key] + trans_amount

    spending = []
    for key, value in spending_dict.items():
        spending.append(Spending(key[0], key[1], round(value, 2)))
    for key, value in month_spending_dict.items():
        spending.append(Spending(key, "Total", round(value, 2)))
    spending = sorted(spending, reverse=True)
    return spending


@app.route('/overview')
def overview():
    accounts = Account.query.filter_by(user_id=current_user.id)
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(
        Transaction.account_id.asc(), Transaction.transaction_date.desc())
    spending = calculate_spending(transactions)
    return render_template('overview.html', accounts=accounts, transactions=transactions,
        spending=spending)


def get_thirdparty_credentials(api_url, login, pwd):
    request_url = "{}/login?account_login={}&account_password={}".format(api_url, login, pwd)
    response = requests.get(request_url)
    return response


def get_thirdparty_accountinfo(api_url, account_login, account_password_hash):
    request_url = "{}/account?account_login={}&account_password_hash={}".format(
        api_url, account_login, account_password_hash)
    response = requests.get(request_url, timeout=3)
    return response


def get_thirdparty_transactions(api_url, account_id):
    request_url = "{}/transactions?account_id={}".format(api_url, account_id)
    response = requests.get(request_url, timeout=3)
    return response


def determine_category(seller):
    r = redis.Redis()
    try:
        category = r.get(seller)
        return "Uncategorized" if not category else category.decode('utf-8')
    except:
        return "Uncategorized"

@app.route('/link_account', methods=['GET', 'POST'])
def link_account():

    form = AccountForm()

    if form.validate_on_submit():

        # validate third party credentials
        api_url = institutions.get(form.institution.data)
        login = form.login.data
        pwd = form.password.data

        try:
            response = get_thirdparty_credentials(api_url, login, pwd)
        except:
            institution = form.institution.data
            flash("Couldn't connect to third-party-api (institution = {})".format(institution))
            return render_template('account.html', form=form, institutions=institutions.keys())

        if response.status_code == 400 or response.status_code == 401:
            flash("Invalid login or password.")
            return render_template('account.html', form=form, institutions=institutions.keys())

        # get third party account info
        api_url = institutions.get(form.institution.data)
        account_login, account_password_hash = response.json().values()
        account_resp = get_thirdparty_accountinfo(api_url, account_login, account_password_hash)

        # get third party transactions
        api_url = institutions.get(form.institution.data)
        transactions_resp = get_thirdparty_transactions(api_url, account_resp.json().get("id"))

        # add account record
        account = Account(created_at=datetime.now(),
                          last_update=datetime.now(),
                          account_institution=form.institution.data,
                          account_name=form.account_name.data,
                          account_url=institutions.get(form.institution.data),
                          account_login=account_login,
                          account_password_hash=account_password_hash,
                          account_balance=account_resp.json().get("balance"),
                          third_party_id=account_resp.json().get("id"),
                          user_id=current_user.id)
        db.session.add(account)
        db.session.commit()

        # add transaction records (multiple)
        for transaction_resp in transactions_resp.json().get("json_list"):
            date_fmt = "%a, %d %b %Y %H:%M:%S %Z"
            transaction_date = datetime.strptime(transaction_resp.get("date"), date_fmt)
            transaction = Transaction(transaction_date=transaction_date,
                transaction_seller=transaction_resp.get("seller"),
                transaction_amount=transaction_resp.get("amount"),
                category=determine_category(transaction_resp.get("seller")),
                customized=False,
                third_party_id=transaction_resp.get("id"),
                user_id=current_user.id,
                account_id=account.id)
            db.session.add(transaction)
        db.session.commit()

        flash('Congratulations, you have successfully linked your account!')

        return redirect(url_for('overview'))

    return render_template('account.html', form=form, institutions=institutions.keys())


@app.route('/update_category/<transaction_id>', methods=['GET', 'POST'])
def update_category(transaction_id):

    transaction = Transaction.query.filter_by(id=transaction_id).first()

    form = CategoryForm()

    if form.validate_on_submit():

        category = form.category.data
        transaction.category = category
        transaction.customized = True
        db.session.commit()

        flash("Updated transaction category to {}".format(category))

        return redirect(url_for('overview'))
    
    return render_template('category.html', form=form, categories=categories, transaction=transaction)


@app.route('/refresh_account/<account_id>', methods=['GET', 'POST'])
def refresh_account(account_id):
    
    account = Account.query.filter_by(id=account_id).first()

    # get third party account info
    api_url = account.account_url
    login = account.account_login
    password_hash = account.account_password_hash

    try:
        account_resp = get_thirdparty_accountinfo(api_url, login, password_hash)
    except:
        institution = account.account_institution
        flash("Couldn't connect to third-party-api (institution = {})".format(institution))
        return overview()

    # get third party transactions
    api_url = account.account_url
    transactions_resp = get_thirdparty_transactions(api_url, account.third_party_id)

    # update account record
    account.account_balance = account_resp.json().get("balance")
    account.last_update = datetime.now()
    db.session.commit()

    # add new transaction records (multiple)
    for transaction_resp in transactions_resp.json().get("json_list"):
        tid = transaction_resp.get("id")
        existing = Transaction.query.filter_by(third_party_id=tid).first()
        if existing is None:
            date_fmt = "%a, %d %b %Y %H:%M:%S %Z"
            transaction_date = datetime.strptime(transaction_resp.get("date"), date_fmt)
            transaction = Transaction(transaction_date=transaction_date,
                transaction_seller=transaction_resp.get("seller"),
                transaction_amount=transaction_resp.get("amount"),
                category=determine_category(transaction_resp.get("seller")),
                customized=False,
                third_party_id=transaction_resp.get("id"),
                user_id=current_user.id,
                account_id=account.id)
            db.session.add(transaction)
    db.session.commit()
    flash("Refreshed account {} at {}".format(account, datetime.now()))
    return overview()


@app.route('/api/v1/user', methods=['POST'])
def add_user():
    u = User(username=request.json.get("username"),
             email=request.json.get("email"),
             password_hash=request.json.get("password_hash"))
    db.session.add(u)
    db.session.commit()

    return jsonify({"status": "OK"}), 200


@app.route('/api/v1/account', methods=['POST'])
def add_account():
    u = User.query.filter_by(username=request.json.get("username")).first()
    user_id = u.id

    # calculate password hash
    password = request.json.get("account_password")
    hashvalue = hashlib.md5(password.encode())
    hexvalue = hashvalue.hexdigest()

    account = Account(created_at=datetime.now(),
                      last_update=datetime.now(),
                      account_url=request.json.get("account_url"),
                      account_login=request.json.get("account_login"),
                      account_password_hash=hexvalue,
                      user_id=user_id)
    db.session.add(account)
    db.session.commit()

    return jsonify({"status": "OK"}), 200


@app.route('/api/v1/transaction', methods=['POST'])
def add_transaction():
    u = User.query.filter_by(username=request.json.get("username")).first()
    user_id = u.id

    transaction = Transaction(created_at=datetime.now(),
                              seller=request.json.get("seller"),
                              amount=request.json.get("amount"),
                              user_id=user_id)
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"status": "OK"}), 200
