from .base_model import ArrangoDBModel


class Account(ArrangoDBModel):

    __NAME__ = "Accounts"

    def __init__(self):
        pass
