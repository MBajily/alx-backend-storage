#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection.
        name (str): The school name to update.
        topics (list): The list of topics approached in
        the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )


if __name__ == "__main__":
    client = MongoClient()
    school_collection = client.my_db.school
    p1 = "Holberton school"
    p2 = ["Sys admin", "AI", "Algorithm"]
    update_topics(school_collection, p1, p2)

    schools = list_all(school_collection)
    for school in schools:
        p1 = school.get('_id')
        p2 = school.get('name')
        p3 = school.get('topics', "")
        print("[{}] {} {}".format(p1, p2, p3))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        p1 = school.get('_id')
        p2 = school.get('name')
        p3 = school.get('topics', "")
        print("[{}] {} {}".format(p1, p2, p3))
