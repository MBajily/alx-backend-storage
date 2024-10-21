#!/usr/bin/env python3
"""
Returns all students sorted by average score
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection.

    Returns:
        list: A list of student documents sorted by average score.
    """
    students = list(mongo_collection.find())
    for student in students:
        total_score = sum(topic['score'] for topic in student['topics'])
        student['averageScore'] = total_score / len(student['topics'])
    students.sort(key=lambda x: x['averageScore'], reverse=True)
    return students


if __name__ == "__main__":
    client = MongoClient()
    students_collection = client.my_db.students

    j_students = [
        {'name': "John", 'topics': [
            {'title': "Algo", 'score': 10.3},
            {'title': "C", 'score': 6.2},
            {'title': "Python", 'score': 12.1}
        ]},
        {'name': "Bob", 'topics': [
            {'title': "Algo", 'score': 5.4},
            {'title': "C", 'score': 4.9},
            {'title': "Python", 'score': 7.9}
        ]},
        {'name': "Sonia", 'topics': [
            {'title': "Algo", 'score': 14.8},
            {'title': "C", 'score': 8.8},
            {'title': "Python", 'score': 15.7}
        ]},
        {'name': "Amy", 'topics': [
            {'title': "Algo", 'score': 9.1},
            {'title': "C", 'score': 14.2},
            {'title': "Python", 'score': 4.8}
        ]},
        {'name': "Julia", 'topics': [
            {'title': "Algo", 'score': 10.5},
            {'title': "C", 'score': 10.2},
            {'title': "Python", 'score': 10.1}
        ]}
    ]
    for j_student in j_students:
        insert_school(students_collection, **j_student)

    students = list_all(students_collection)
    for student in students:
        p1 = student.get('_id')
        p2 = student.get('name')
        p3 = student.get('topics')
        print("[{}] {} - {}".format(p1, p2, p3))

    top_students = top_students(students_collection)
    for student in top_students:
        p1 = student.get('_id')
        p2 = student.get('name')
        p3 = student.get('averageScore')
        print("[{}] {} => {}".format(p1, p2, p3))
