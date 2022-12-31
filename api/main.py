import api.router
import asyncio
from fastapi import FastAPI
from db.database import Database
app = FastAPI()

db = Database()

@app.get('/')
async def Home():
    return "welcome home"


# @app.get('/users/getUserByName/:name')
# def getUserByName(user: User):
#     ...


app.include_router(api.router.route)
asyncio.create_task(api.router.consume())
