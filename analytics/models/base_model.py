from datetime import datetime

from pydantic import BaseModel


class ArrangoDBModel(BaseModel):
    _id: str
    _created_at: datetime = datetime.now()
    _updated_at: datetime = datetime.now()

    @classmethod
    def create(cls):
        pass
