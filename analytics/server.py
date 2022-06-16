import logging

from fastapi import FastAPI
from starlette import status

from .models import initialize_database


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

initialize_database()

app = FastAPI()