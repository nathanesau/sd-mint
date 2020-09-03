# mint-app

API reference:

| Endpoint | Method | Input |  
| -------- | ------ | ----- |
| /api/v1/user | POST | ``{"username":"nathan","email":"nathanesau1@gmail.com","password_hash":"abcdefgh"}`` |
| /api/v1/account | POST | ``{"username":nathan,"account_url":"bar","account_login":"baz","account_password":"qux"}`` |
| /api/v1/transaction | POST | ``{"seller":"walmart","amount":55.73,"username":"nathan"}`` |

API examples:

```bash
# /api/v1/user
curl -H "Content-Type: application/json" --request POST --data '{"username":"nathan","email":"nathanesau1@gmail.com","password_hash":"abcdefgh"}' "http://127.0.0.1:5000/api/v1/user"

# /api/v1/account
curl -H "Content-Type: application/json" --request POST --data '{"user_id":"nathan","account_url":"bar","account_login":"baz","account_password":"qux"}' "http://127.0.0.1:5000/api/v1/account"

# /api/v1/transaction
curl -H curl -H "Content-Type: application/json" --request POST --data '{"username": "nathan", "seller":"walmart","amount":55.73}' "http://127.0.0.1:5000/api/v1/transaction"
```
