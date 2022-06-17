import logging
import os
import sys
from typing import List

from pyArango.connection import Connection
from pyArango.database import Database

from .account import Account
from .session import Session

__all__ = [
    'initialize_database',
    'create_connection',
    'Account',
    'Session'
]

DATABASE_URL = os.getenv("DATABASE_URL", "http://127.0.0.1:8529")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "test123")
DATABASE_NAME = os.getenv("DATABASE_NAME", "AGIAnalysis")

COLLECTIONS_NAME = [Account, Session]

logger = logging.getLogger(sys.modules[__name__].__name__)


# noinspection SqlNoDataSourceInspection
def initialize_database():
    connection = Connection(arangoURL=DATABASE_URL, username=DATABASE_USERNAME, password=DATABASE_PASSWORD)
    database_version = connection.getVersion()
    logger.info(f"ArangoDB version: {database_version}")

    if not connection.hasDatabase(DATABASE_NAME):
        connection.createDatabase(DATABASE_NAME)
        logger.info(f"Create database {DATABASE_NAME} in ArangoDB")

    _initialize_collections(connection, COLLECTIONS_NAME)

    connection.disconnectSession()


class create_connection:

    def __enter__(self):
        self.connection = Connection(arangoURL=DATABASE_URL, username=DATABASE_USERNAME, password=DATABASE_PASSWORD)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.disconnectSession()


# noinspection PyUnresolvedReferences
def _initialize_collections(connection: Connection, collections_name: List[str]):
    database = Database(connection, DATABASE_NAME)

    for collection_name in collections_name:
        if not database.hasCollection(collection_name.__tablename__):
            database.createCollection(name=collection_name.__tablename__)
            logger.info(f"Create collection: {collection_name.__tablename__}")
