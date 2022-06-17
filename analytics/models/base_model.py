from datetime import datetime
from typing import Dict

from pydantic import BaseModel

from .. import models

TABLE_NAME = "__tablename__"
CALLBACK_BEFORE_SAVE = "__before_save__"


class ArrangoDBModel(BaseModel):
    _id: str
    _key: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def save(self):
        with models.create_connection() as connection:
            if hasattr(self, CALLBACK_BEFORE_SAVE):
                getattr(self, CALLBACK_BEFORE_SAVE)()
                collection_name = getattr(self.__class__, TABLE_NAME)
                connection[models.DATABASE_NAME][collection_name] \
                    .createDocument(initDict=self.dict()).save()

    @classmethod
    def create(cls, init_dict: Dict):
        with models.create_connection() as connection:
            collection_name = getattr(cls.__class__, TABLE_NAME)
            connection[models.DATABASE_NAME][collection_name] \
                .createDocument(initDict=init_dict).save()

    @classmethod
    def find_by_key(cls, key: int):
        return cls.find_first({"_key": key})

    @classmethod
    def find_first(cls, predicate: Dict):
        collection_name = getattr(cls, TABLE_NAME)
        with models.create_connection() as connection:
            doc = connection[models.DATABASE_NAME][collection_name].fetchFirstExample(predicate)
            if len(doc) == 0:
                return None
            else:
                return doc[0]

    @classmethod
    def find_all(cls, predicate: Dict):
        collection_name = getattr(cls, TABLE_NAME)
        with models.create_connection() as connection:
            return connection[models.DATABASE_NAME][collection_name].fetchExample(predicate)
