#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        topic (str): The topic searched.

    Returns:
        list: A list of school documents having the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    client = MongoClient()
    school_collection = client.my_db.school

    j_schools = [
        {'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
        {'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        {'name': "UCLA", 'topics': ["C", "Python"]},
        {'name': "UCSD", 'topics': ["Cassandra"]},
        {'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
