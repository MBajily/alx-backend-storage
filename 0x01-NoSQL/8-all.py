#!/usr/bin/env python3
"""
Lists all documents in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection.

    Returns:
        list: A list of all documents in the collection.
    """
    documents = list(mongo_collection.find())
    return documents


if __name__ == "__main__":
    client = MongoClient()
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
