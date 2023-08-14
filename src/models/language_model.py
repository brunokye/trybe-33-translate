from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        self.data = data

    # Req. 2
    def to_dict(self):
        return {
            "_id": self.data["_id"],
            "name": self.data["name"],
            "acronym": self.data["acronym"]
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        data = cls._collection.find()
        result = []

        for d in data:
            language = cls(d)
            result.append(language.to_dict())

        return result
