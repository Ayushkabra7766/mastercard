---

## Create Account

## `PUT /accounts/{account_id}`

Description: Create a new account. Fails if the account already exists.

**Request Body:**
```json
{
  "name": "Ayush",
  "description": "Test",
  "balance": 100,
  "active": true
}

curl -X 'PUT' \
  'http://127.0.0.1:8000/accounts/101' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Ayush",
  "description": "Test",
  "balance": 100,
  "active": true
}'

## Response

{
  "name": "Ayush",
  "description": "Test",
  "balance": 100,
  "active": true
}

