import logging

from fastapi import FastAPI
from starlette import status

from .models.account import Account
from .models.base_model import initialize_database

COLLECTIONS_NAME = [Account.__NAME__]


class StaticFileAccessLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        http_status = record.args[-1]
        uri = record.args[-3]
        if int(http_status) == status.HTTP_200_OK:
            return not uri.endswith('.html') and not uri.endswith('.css') \
                   and not uri.endswith('.js') and not uri.endswith('.js.map') and not uri.endswith('ico')
        return False


logging.getLogger("uvicorn.access").addFilter(StaticFileAccessLogFilter())
logging.basicConfig(filename='logging.conf')

app = FastAPI()

initialize_database(COLLECTIONS_NAME)
