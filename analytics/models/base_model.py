import logging
import os

from pyArango.connection import Connection

DATABASE_URL = os.getenv("DATABASE_URL", "http://127.0.0.1:8529")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "test123")
DATABASE_NAME = os.getenv("DATABASE_NAME", "AGIAnalysis")


def initialize_database():
    connection = Connection(arangoURL=DATABASE_URL, username=DATABASE_USERNAME, password=DATABASE_PASSWORD)
    database_version = connection.getVersion()
    logging.info(f"ArangoDB version: {database_version}")
    if not connection.hasDatabase(DATABASE_NAME):
        connection.createDatabase(DATABASE_NAME)
        logging.info(f"Create database {DATABASE_NAME} in ArangoDB")
    connection.disconnectSession()

