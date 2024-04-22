# pylint: disable=R0801
"""
from fastapi import FastAPI
    Library of functions
"""
from os import getenv

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session


def get_db_url_prod() -> str:
    """get db url"""
    db_name = getenv('PG_DB_NAME')
    db_user = getenv('PG_DB_USER')
    db_pass = getenv('PG_DB_PASS')
    db_host = getenv('PG_DB_HOST')
    db_port = getenv('PG_DB_PORT')
    return f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


def get_db_url_test() -> str:
    """get db url"""
    db_name = getenv('PG_DB_NAME_TEST')
    db_user = getenv('PG_DB_USER')
    db_pass = getenv('PG_DB_PASS')
    db_host = getenv('PG_DB_HOST')
    db_port = getenv('PG_DB_PORT')
    return f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


def get_db_engine(url: str) -> Engine:
    """creates db engine"""
    return create_engine(url)


def get_db_session(url: str) -> Session:
    """get db session"""
    return Session(get_db_engine(url))
