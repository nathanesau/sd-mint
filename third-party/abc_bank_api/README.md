# abc_bank_api

API reference:

| Endpoint | Request | Arguments | Response | 
| -------- | ------- | --------- | -------- |
| /api/v1/login?account_login=123456781234&account_password=foobar | GET | N/A | ``{"account_login": "123456781234", "account_password_hash": "somehash"}``
| /api/v1/account?account_login=123456781234&account_password_hash=foobar | GET | N/A | ``{"id": 1, "balance": 1013.28}``
| /api/v1/transactions?account_id=1 | GET | N/A | ``[{"transaction_date": "2019/08/03, "transaction_seller": "walmart", "transaction_amount": 12.04, "account_id": 1}]``

API tests:

```bash
# /api/v1/login
curl "http://165.22.234.253:5001/api/v1/login?account_login=123456781234&account_password=abc_savings_nathan"

# /api/v1/account
curl "http://localhost:5001/api/v1/account?account_login=123456781234&account_password_hash=pbkdf2:sha256:150000\$lEFOkCJM\$6a8c24faf7db28b9f507fb6d0f8d202c1c0132d5c29748daea1baebab8fa8dea"

# /api/v1/transactions
curl "http://localhost:5001/api/v1/transactions?account_id=2"
```

Running API:

```bash
cd third-party/abc_bank_api
python abc_bank_api.py
```