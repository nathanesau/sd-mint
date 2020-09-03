from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SCHEDULER_API_ENABLED'] = True
app.config['JOBS'] = [{'id':'cs','func':'app.jobs:cs_task','trigger':'interval','seconds':30}]
app.config['SECRET_KEY'] = 'vZ9YVje1aU'
app.config['THIRD_PARTY_API_URL'] = {
    "abc_bank": "http://localhost:5001/api/v1",
    "xyz_bank": "http://localhost:5002/api/v1",
    "xyz_trade_api": "http://localhost:5003/api/v1"
}
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# background scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

from app import routes, models