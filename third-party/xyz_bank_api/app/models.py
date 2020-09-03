from app import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_login = db.Column(db.String(32), nullable=False)
    account_password_hash = db.Column(db.String(64), nullable=False)
    account_balance = db.Column(db.Float, nullable=False)
    account_description = db.Column(db.String(255), nullable=False)


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.Date, nullable=False)
    transaction_seller = db.Column(db.String(32), nullable=False)
    transaction_amount = db.Column(db.Float, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
