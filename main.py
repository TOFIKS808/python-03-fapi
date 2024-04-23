"""
    API
"""

from fastapi import FastAPI
from src.api.users import users_get_item
from src.api.company import company_get_item
from src.api.address import address_get_item
from src.api.geo import geo_get_item
from src.api.post import posts_get_item
from src.api.comment import comments_get_item

app = FastAPI()


@app.get("/users/{id}", tags=["Users"])
def api_users_get_item(id: int):
    """ get user endpoint"""
    return users_get_item(id)

@app.get("/companies/{id}", tags=["Company"])
def api_users_get_item(id: int):
    """ get company endpoint"""
    return company_get_item(id)

@app.get("/addresses/{id}", tags=["Address"])
def api_users_get_item(id: int):
    """ get address endpoint"""
    return address_get_item(id)

@app.get("/geo/{id}", tags=["Geo"])
def api_users_get_item(id: int):
    """ get geo endpoint"""
    return geo_get_item(id)


@app.get("/posts/{id}", tags=["Post"])
def api_posts_get_item(id: int):
    """ get posts endpoint"""
    return posts_get_item(id)

@app.get("/comments/{id}", tags=["Comment"])
def api_posts_get_item(id: int):
    """ get comment endpoint"""
    return comments_get_item(id)
