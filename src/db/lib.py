# pylint: disable=R0801
"""
from fastapi import FastAPI
    Library of functions
"""
from os import getenv

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session


DB_URL = getenv("DB_URL")

def get_db_engine(url: str) -> Engine:
    """creates db engine"""
    return create_engine(url)


def get_db_session(url: str) -> Session:
    """get db session"""
    return Session(get_db_engine(url))
