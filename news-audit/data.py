from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
from itertools import chain

load_dotenv()
route = getenv("MONGO_PATH")
client = MongoClient(route)


def send_to_mongo(database_name: str, collection: str, data: dict) -> str:
    """Sends one document to a given collection in MongoDB"""
    db = client[database_name]
    col = db[collection]
    mongo_object_id = col.insert_one(data)

    print(mongo_object_id)
    print(mongo_object_id.inserted_id)

    return "Document added to MongoDB."


def search_documents(database_name: str, collection: str, data: dict = None) -> list:
    """Returns all documents matching search query `data`
    :rtype: object
    """
    db = client[database_name]
    col = db[collection]
    cursor = col.find(data)
    return list(cursor)


def dict_union(*args):
    return dict(chain.from_iterable(d.items() for d in args))
