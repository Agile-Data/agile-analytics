from fastapi import FastAPI


async def create():
    pass


async def destroy():
    pass


def initialize_sessions(app: FastAPI):
    app.add_api_route('/sessions', create, methods=['POST'])
    app.add_api_route('/sessions', destroy, methods=['DELETE'])
