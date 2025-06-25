from typing import Dict, Optional
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel


class Account(BaseModel):
    name: str
    description: Optional[str] = None
    balance: float
    active: bool = True


app = FastAPI()

# In-memory data store
accounts = dict()


# Helper functions
async def get_account(account_id: int) -> Optional[Account]:
    if account_id in accounts:
        return Account(**accounts[account_id])  # ✅ fix here
    return None


async def add_account(account_id: int, account: Account) -> Optional[Account]:
    if account_id in accounts:
        return None
    accounts[account_id] = account.dict()
    return Account(**accounts[account_id])  # ✅ fix here


async def delete_account(account_id: int) -> Optional[bool]:
    if account_id in accounts:
        return True
    return None


# Routes

@app.get("/healthz", response_model=Dict[str, bool])
async def get_health(request: Request):
    return {"status": True}


@app.get("/accounts/{account_id}", response_model=Account)
async def read_account(account_id: int):
    res = await get_account(account_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return res


@app.put("/accounts/{account_id}", response_model=Account, status_code=201)
async def create_account(account_id: int, account: Account):
    res = await add_account(account_id, account)
    if res is None:
        raise HTTPException(status_code=409, detail="Account exists")
    return res


@app.delete("/accounts/{account_id}", status_code=200)
async def remove_account(account_id: int):
    deleted = await delete_account(account_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Account not found")
    del accounts[account_id]
    return {"msg": "Successful"}
