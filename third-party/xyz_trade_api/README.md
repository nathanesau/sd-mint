# xyz_trade_api

API reference:

| Endpoint | Request | Arguments | Response |
| -------- | ------- | --------- | -------- |
| /api/v1/login?account_login=123456781234&account_password=foobar | GET | N/A | ``{"account_login": "123456781234", "account_password_hash": "somehash"}``
| /api/v1/account?account_login=123456781234&account_password_hash=foobar | GET | N/A | ``{"id": 1, "balance": 1013.28}``
| /api/v1/transactions?account_id=1 | GET | N/A | ``[{"transaction_date": "2019/08/03, "transaction_seller": "walmart", "transaction_amount": 12.04, "account_id": 1}]``

API tests:

```bash
# /api/v1/login
curl "http://localhost:5003/api/v1/login?account_login=123456781234&account_password=xyz_trade_nathan"

# /api/v1/account
curl "http://localhost:5003/api/v1/account?account_login=123456781234&account_password_hash=pbkdf2:sha256:150000\$n2AuFT22\$4a01dd1f4fd8231b8c4ee41500c1fc6d64adf994faf020e471c5029b1083080d"

# /api/v1/transactions
curl "http://localhost:5003/api/v1/transactions?account_id=2"
```

Running API:

```bash
cd third-party/xyz_trade_api
python xyz_trade_api.py
```