import logging

from fastapi import FastAPI

from analytics.models.base_model import initialize_database

logging.basicConfig(filename='logging.conf')

app = FastAPI()

initialize_database()