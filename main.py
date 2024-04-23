"""
    API
"""

from fastapi import FastAPI
from src.api.users import users_get_item

app = FastAPI()


@app.get("/users/{id}", tags=["Users"])
def api_users_get_item(id: int):
    """ get user endpoint"""
    return users_get_item(id)