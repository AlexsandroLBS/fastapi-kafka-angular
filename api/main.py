import api.router
import asyncio
from api.schema import User
from fastapi import FastAPI
from db.database import Database


app = FastAPI()

db = Database()

@app.get('/')
async def Home():
    return "welcome home"

@app.get('/users/getLogin/')
def userLogin(user: User):
    return db.getLogin(user)


@app.post('/users/createAccount/')
def userSignUp(user: User):
    return db.createAccount(user)


app.include_router(api.router.route)
asyncio.create_task(api.router.consume())
