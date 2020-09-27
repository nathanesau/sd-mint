from app import app, db
from app.models import User, Transaction

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
