from datetime import datetime

from pydantic import BaseModel

from .. import models

TABLE_NAME = "__tablename__"
BEFORE_SAVE = "__before_save__"


class ArrangoDBModel(BaseModel):
    _id: str
    created_at: datetime
    updated_at: datetime

    def save(self):
        with models.create_connection() as connection:
            if hasattr(self, BEFORE_SAVE):
                getattr(self, BEFORE_SAVE)()
                collection_name = getattr(self, TABLE_NAME)
                connection[models.DATABASE_NAME][collection_name]\
                    .createDocument(initDict=self.dict()).save()


