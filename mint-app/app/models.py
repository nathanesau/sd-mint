from app import db, login
from flask_login import UserMixin
from hashlib import md5


categories = {
    "Auto-Transport": "",
    "Bills-Utilities": "",
    "Business-Services": "",
    "Education": "",
    "Entertainment": "",
    "Fees-Charges": "",
    "Financial": "",
    "Food-Dining": "",
    "Gifts-Donations": "",
    "Health-Fitness": "",
    "Home": "",
    "Income": "",
    "Kids": "",
    "Misc-Expenses": "",
    "Pets": "",
    "Shopping": "",
    "Taxes": "",
    "Transfer": "",
    "Travel": "",
    "Uncategorized": "",
    "Auto-Insurance": "Auto-Transport",
    "Auto-Payment": "Auto-Transport",
    "Gas-Fuel": "Auto-Transport",
    "Parking": "Auto-Transport",
    "Public-Transportation": "Auto-Transport",
    "Service-Parts": "Auto-Transport",
    "Home-Phone": "Bills-Utilities",
    "Internet" :"Bills-Utilities",
    "Mobile-Phone": "Bills-Utilities",
    "Telivision": "Bills-Utilities",
    "Utilities": "Bills-Utilities",
    "Advertising": "Business-Services",
    "Legal": "Business-Services",
    "Office-Supplies": "Business-Services",
    "Printing": "Business-Services",
    "Shipping": "Business-Services",
    "Books-Supplies": "Education",
    "Student-Loan": "Education",
    "Tuition": "Education",
    "Amusement": "Entertainment",
    "Arts": "Entertainment",
    "Movies-DVDs": "Entertainment",
    "Music": "Entertainment",
    "Newspapers-Magazines": "Entertainment",
    "ATM-Fee": "Fees-Charges",
    "Bank-Fee": "Fees-Charges",
    "Finance-Charge": "Fees-Charges",
    "Late-Fee": "Fees-Charges",
    "Service-Fee": "Fees-Charges",
    "Trade-Commissions": "Fees-Charges",
    "Financial-Advisor": "Financial",
    "Life-Insurance": "Financial",
    "Alcohol-Bars": "Food-Dining",
    "Coffee-Shops": "Food-Dining",
    "Fast-Food": "Food-Dining",
    "Groceries": "Food-Dining",
    "Restaurants": "Food-Dining",
    "Charity": "Gifts-Donations",
    "Gift": "Gifts-Donations",
    "Dentist": "Health-Fitness",
    "Doctor": "Health-Fitness",
    "Eyecare": "Health-Fitness",
    "Gym": "Health-Fitness",
    "Health-Insurance": "Health-Fitness",
    "Pharmacy": "Health-Fitness",
    "Sports": "Health-Fitness",
    "Furnishings": "Home",
    "Home-Improvement": "Home",
    "Home-Insurance": "Home",
    "Home-Services": "Home",
    "Home-Supplies": "Home",
    "Lawn-Garden": "Home",
    "Mortgage-Rent": "Home",
    "Bonus": "Income",
    "Interest-Income": "Income",
    "Paycheque": "Income",
    "Reimbursement": "Income",
    "Rental-Income": "Income",
    "Returned-Purchase": "Income",
    "Allowance": "Kids",
    "Baby-Supplies": "Kids",
    "Babysitter-Daycare": "Kids",
    "Child-Support": "Kids",
    "Kids-Activities": "Kids",
    "Toys": "Kids",
    "Conference": "Misc-Expenses",
    "Hair": "Personal-Care",
    "Laundry": "Personal-Care",
    "Spa-Massage": "Personal-Care",
    "Pet-Food-Supplies": "Pets",
    "Pet-Grooming": "Pets",
    "Veterinary": "Pets",
    "Books": "Shopping",
    "Clothing": "Shopping",
    "Electronics-Software": "Shopping",
    "Hobbies": "Shopping",
    "Sporting-Goods": "Shopping",
    "Federal-Tax": "Taxes",
    "Local-Tax": "Taxes",
    "Property-Tax": "Taxes",
    "Sales-Tax": "Taxes",
    "Provincial-Tax": "Taxes",
    "Credit-Card-Payment": "Transfer",
    "Transfer-for-Cash-Spending": "Transfer",
    "Air-Travel": "Travel",
    "Hotel": "Travel",
    "Rental-Car-Taxi": "Travel",
    "Vacation": "Travel",
    "Cash-ATM": "Uncategorized",
    "Cheque": "Uncategorized"
}


class User(UserMixin, db.Model):
    """
    Same user table design used in the flask-mega-tutorial
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        url = 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
        return url


class Account(db.Model):
    """
    Info obtained from third-party API
    """
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False)
    account_institution = db.Column(db.String(32), nullable=False)
    account_name = db.Column(db.String(32), nullable=False)
    account_url = db.Column(db.String(255), nullable=False)
    account_login = db.Column(db.String(32), nullable=False)
    account_password_hash = db.Column(db.String(128), nullable=False)
    account_balance = db.Column(db.Float, nullable=False)
    third_party_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Account {}>'.format(self.third_party_id)


class Transaction(db.Model):
    """
    Info obtained from third-party API
    """
    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime, nullable=False)
    transaction_seller = db.Column(db.String(32), nullable=False)
    transaction_amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(32), nullable=False)
    customized = db.Column(db.Boolean, nullable=False)
    third_party_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                                       nullable=False)

    def __repr__(self):
        return '<Transaction {}>'.format(self.third_party_id)


class Spending:
    """
    Info calculated using transactions
    """
    def __init__(self, month_year, category, amount):
        self.month_year = month_year
        self.category = category
        self.amount = amount

    def __lt__(self, other): # ascen
        if self.month_year < other.month_year:
            return True
        elif self.month_year == other.month_year:
            if self.category !=' Total' and  other.category == 'Total':
                return False
            return self.category > other.category
        return False

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
