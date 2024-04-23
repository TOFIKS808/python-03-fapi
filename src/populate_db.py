# pylint: disable=R0801
"""
    Data base populating
"""
from os import getenv
import requests as rq
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, drop_database, create_database

from Model import Base, User, Company, Address, Geo, Post, Comment, Album, Photo, Todo


def create_db(url: str) -> None:
    """create new db, drop if exists"""
    engine = create_engine(url)
    print(url)
    if database_exists(engine.url):
        drop_database(engine.url)

    create_database(engine.url)

def create_schema(url: str) -> None:
    """create tables"""
    engine = create_engine(url)
    Base.metadata.drop_all(engine)
    # exit()
    Base.metadata.create_all(engine)


def endpoint_users(url: str) -> None:
    """Handling user endpoints"""
    result = rq.get("https://jsonplaceholder.typicode.com/users", timeout=2)
    engine = create_engine(url)
    data = []
    for user in result.json():
        obj_user = User(
            id=user['id'],
            name=user['name'],
            username=user['username'],
            email=user['email'],
            phone=user['phone'],
            website=user['website'],
            company=Company(
                id=user['id'],
                name=user["company"]["name"],
                catch_phrase=user["company"]["catchPhrase"],
                bs=user["company"]["bs"]
            ),
            address=Address(
                id=user['id'],
                street=user["address"]["street"],
                suite=user["address"]["suite"],
                city=user["address"]["city"],
                zipcode=user["address"]["zipcode"],
                geo=Geo(
                    id=user['id'],
                    lat=user["address"]["geo"]["lat"],
                    long=user["address"]["geo"]["lng"]
                )
            ),
        )
        data.append(obj_user)
    with Session(engine) as session:
        for obj in data:
            session.add(obj)
        session.commit()


def endpoint_posts(url: str) -> None:
    """Handling posts endpoints"""
    result = rq.get("https://jsonplaceholder.typicode.com/posts", timeout=2)
    engine = create_engine(url)
    data = []
    for post in result.json():
        obj_posts = Post(
            id=post['id'],
            user_id=post['userId'],
            title=post['title'],
            body=post['body'],
        )
        data.append(obj_posts)
    with Session(engine) as session:
        for obj in data:
            session.add(obj)
        session.commit()


def endpoint_comments(url: str) -> None:
    """Handling comments endpoints"""
    result = rq.get("https://jsonplaceholder.typicode.com/comments", timeout=2)
    engine = create_engine(url)
    data = []
    for comment in result.json():
        obj_comments = Comment(
            id=comment['id'],
            post_id=comment['postId'],
            name=comment['name'],
            email=comment['email'],
            body=comment['body'],
        )
        data.append(obj_comments)
    with Session(engine) as session:
        for obj in data:
            session.add(obj)
        session.commit()


def endpoint_albums(url: str) -> None:
    """Handling albums endpoints"""
    result = rq.get("https://jsonplaceholder.typicode.com/albums", timeout=2)
    engine = create_engine(url)
    data = []
    for album in result.json():
        obj_album = Album(
            id=album['id'],
            user_id=album['userId'],
            title=album['title'],
        )
        data.append(obj_album)
    with Session(engine) as session:
        for obj in data:
            session.add(obj)
        session.commit()


def endpoint_photos(url: str) -> None:
    """Handling photos endpoints"""
    result = rq.get("https://jsonplaceholder.typicode.com/photos", timeout=2)
    engine = create_engine(url)
    data = []
    for photo in result.json():
        obj_photos = Photo(
            id=photo['id'],
            album_id=photo['albumId'],
            title=photo['title'],
            url=photo['url'],
            thumbnail_url=photo['thumbnailUrl'],
        )
        data.append(obj_photos)
    with Session(engine) as session:
        for obj in data:
            session.add(obj)
        session.commit()


def endpoint_todos(url: str) -> None:
    """Handling todos endpoints"""
    result = rq.get("https://jsonplaceholder.typicode.com/todos", timeout=2)
    engine = create_engine(url)
    data = []
    for todo in result.json():
        obj_photos = Todo(
            id=todo['id'],
            user_id=todo['userId'],
            title=todo['title'],
            completed=todo['completed'],
        )
        data.append(obj_photos)
    with Session(engine) as session:
        for obj in data:
            session.add(obj)
        session.commit()


if __name__ == '__main__':
    DB_URL = getenv("DB_URL")
    create_db(DB_URL)
    create_schema(DB_URL)
    endpoint_users(DB_URL)
    endpoint_posts(DB_URL)
    endpoint_comments(DB_URL)
    endpoint_albums(DB_URL)
    endpoint_photos(DB_URL)
    endpoint_todos(DB_URL)
