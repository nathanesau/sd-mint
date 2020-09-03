# xyz_bank_api

API reference:

| Endpoint | Request | Arguments | Response |
| -------- | ------- | --------- | -------- |
| /api/v1/login?account_login=123456781234&account_password=foobar | GET | N/A | ``{"account_login": "123456781234", "account_password_hash": "somehash"}``
| /api/v1/account?account_login=123456781234&account_password_hash=foobar | GET | N/A | ``{"id": 1, "balance": 1013.28}``
| /api/v1/transactions?account_id=1 | GET | N/A | ``[{"transaction_date": "2019/08/03, "transaction_seller": "walmart", "transaction_amount": 12.04, "account_id": 1}]``

API tests:

```bash
# /api/v1/login
curl "http://localhost:5002/api/v1/login?account_login=123456781234&account_password=xyz_bank_nathan"

# /api/v1/account
curl "http://localhost:5002/api/v1/account?account_login=123456781234&account_password_hash=pbkdf2:sha256:150000\$FRb1SnZg\$6174439c41665d33166cae4ce22a5c080dbcdd73813712f1123180be08271188"

# /api/v1/transactions
curl "http://localhost:5002/api/v1/transactions?account_id=2"
```

Running API:

```bash
cd third-party/xyz_bank_api
python xyz_bank_api.py
```