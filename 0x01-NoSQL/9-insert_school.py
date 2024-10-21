#!/usr/bin/env python3
"""
Inserts a new document in a MongoDB collection
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        **kwargs: Arbitrary keyword arguments to be inserted as the document.

    Returns:
        str: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)


if __name__ == "__main__":
    client = MongoClient()
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
