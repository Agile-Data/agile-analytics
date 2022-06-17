import hashlib
import os
from typing import Optional

from .base_model import ArrangoDBModel

ROOT_PASSWORD = os.getenv("ROOT_PASSWORD", "agidata.io")


class Account(ArrangoDBModel):
    __tablename__ = "Accounts"

    name: str
    login: str
    password: str
    password_digest: Optional[str]
    role: str
    email: Optional[str] = None

    @classmethod
    def reset_password(cls, login: str, old_password: str, new_password: str):
        pass

    def authenticate(self, login: str, password: str) -> bool:
        return self.__class__.find_first({"login": login, "password_digest": encode_password(password)}) is not None

    def __before_save__(self):
        self.password_digest = encode_password(self.password)
        self.password = "Encrypted"


def encode_password(password: str) -> str:
    md5 = hashlib.md5()
    md5.update(password.encode(encoding='utf-8'))
    return md5.hexdigest()


def initialize_root():
    if Account.find_first({"name": "root"}) is None:
        Account(
            name="root",
            login="root",
            password=ROOT_PASSWORD,
            role="root"
        ).save()
