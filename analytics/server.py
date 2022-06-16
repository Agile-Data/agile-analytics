import logging

from fastapi import FastAPI
from starlette import status

from .controllers import initialize_static_file_route, initialize_gzip, initialize_controllers
from .models import initialize_database


class StaticFileAccessLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        http_status = record.args[-1]
        uri = record.args[-3]
        static_files_suffix = ['png', 'html', 'css', 'js', 'map', 'ico']
        if int(http_status) == status.HTTP_200_OK:
            return uri.split('.')[-1] not in static_files_suffix
        return False


logging.getLogger("uvicorn.access").addFilter(StaticFileAccessLogFilter())
logging.basicConfig(filename='logging.conf')

app = FastAPI()

initialize_database()
initialize_static_file_route(app)
initialize_gzip(app)
initialize_controllers(app)
