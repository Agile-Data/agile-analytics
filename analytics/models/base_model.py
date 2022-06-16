import logging
import os
from typing import List

from pyArango.connection import Connection
from pyArango.database import Database
from pydantic import BaseModel

DATABASE_URL = os.getenv("DATABASE_URL", "http://127.0.0.1:8529")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "test123")
DATABASE_NAME = os.getenv("DATABASE_NAME", "AGIAnalysis")


def initialize_database(collections_name: List[str]):
    connection = Connection(arangoURL=DATABASE_URL, username=DATABASE_USERNAME, password=DATABASE_PASSWORD)
    database_version = connection.getVersion()
    logging.info(f"ArangoDB version: {database_version}")

    if not connection.hasDatabase(DATABASE_NAME):
        connection.createDatabase(DATABASE_NAME)
        logging.info(f"Create database {DATABASE_NAME} in ArangoDB")

    _initialize_schemas(connection, collections_name)

    connection.disconnectSession()


def _initialize_schemas(connection: Connection, collections_name: List[str]):
    database = Database(connection, DATABASE_NAME)

    for collection_name in collections_name:
        if not database.hasCollection(collection_name):
            database.createCollection(name=collection_name)
            logging.info(f"Create collection: {collection_name}")


class ArrangoDBModel(BaseModel):
    pass
