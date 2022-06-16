from fastapi import FastAPI

from .sessions_controller import initialize_sessions


def initialize_static_file_route(app: FastAPI, name="statics"):
    from starlette.staticfiles import StaticFiles

    app.mount("/", StaticFiles(packages=['analytics'], html=True), name=name)


def initialize_gzip(app: FastAPI, minimum_size=1000):
    from starlette.middleware.gzip import GZipMiddleware

    app.add_middleware(GZipMiddleware, minimum_size=minimum_size)


def initialize_controllers(app: FastAPI):
    initialize_sessions(app)

