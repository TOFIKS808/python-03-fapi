"""
    API
"""

from fastapi import FastAPI
from src.api.users import users_get_item, users_get_collection
from src.api.company import company_get_item
from src.api.address import address_get_item
from src.api.geo import geo_get_item
from src.api.post import posts_get_item, posts_delete_item, posts_create_item, posts_update_item
from src.api.comment import comments_get_item
from src.api.album import albums_get_item

from src.ApiModel import PostCreate, PostUpdate

app = FastAPI()


@app.get("/users/{id}", tags=["Users"])
def api_users_get_item(id: int):
    """ get user endpoint"""
    return users_get_item(id)


@app.get("/users/", tags=["Users"])
def api_users_get_collection():
    """ get user endpoint"""
    return users_get_collection()


@app.get("/companies/{id}", tags=["Company"])
def api_companies_get_item(id: int):
    """ get company endpoint"""
    return company_get_item(id)


@app.get("/addresses/{id}", tags=["Address"])
def api_addresses_get_item(id: int):
    """ get address endpoint"""
    return address_get_item(id)


@app.get("/geo/{id}", tags=["Geo"])
def api_geo_get_item(id: int):
    """ get geo endpoint"""
    return geo_get_item(id)


#### POST
@app.get("/posts/{id}", tags=["Post"])
def api_posts_get_item(id: int):
    """ get posts endpoint"""
    return posts_get_item(id)


@app.delete("/posts/{id}", tags=["Post"])
def api_posts_get_item(id: int):
    """ get posts endpoint"""
    return posts_delete_item(id)


@app.get("/posts", tags=["Post"])
def api_posts_get_collection():
    """ get posts endpoint"""


@app.post("/posts", tags=["Post"])
def api_posts_create(post: PostCreate):
    """ create post endpoint"""
    return posts_create_item(post)


@app.put("/posts/{id}", tags=["Post"])
def api_posts_put(id: int, post: PostUpdate):
    """ create posts emdpoint """
    return posts_update_item(id, post)


@app.get("/comments/{id}", tags=["Comment"])
def api_comments_get_item(id: int):
    """ get comment endpoint"""
    return comments_get_item(id)


@app.get("/albums/{id}", tags=["Album"])
def api_albums_get_item(id: int):
    """ get album endpoint"""
    return albums_get_item(id)


@app.get("/photos/{id}", tags=["Photo"])
def api_photos_get_item(id: int):
    """ get photo endpoint"""
    return albums_get_item(id)


@app.get("/todos/{id}", tags=["Todo"])
def api_photos_get_item(id: int):
    """ get todo endpoint"""
    return albums_get_item(id)
