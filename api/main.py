import api.router
import asyncio
from api.schema import User
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import Database


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database()

@app.get('/')
async def Home():
    return "welcome home"

@app.post('/users/login/')
def userLogin(user: User):
    return db.getLogin(user)


@app.post('/users/createAccount/')
def userSignUp(user: User):
    return db.createAccount(user)


app.include_router(api.router.route)
asyncio.create_task(api.router.consume())
