import hashlib
import os
from datetime import datetime
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

    def __before_save__(self):
        self.password_digest = encode_password(self.password)
        self.password = None


def encode_password(password: str) -> str:
    md5 = hashlib.md5()
    md5.update(password.encode(encoding='utf-8'))
    return md5.hexdigest()


def initialize_root():
    Account(
        name="root",
        login="root",
        password=ROOT_PASSWORD,
        role="root",
        email="abc",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ).save()
