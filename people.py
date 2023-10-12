from datetime import datetime
from flask import abort

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

PEOPLE = {
    "Potter": {
        "first_name": "Harry",
        "last_name": "Potter",
        "timestamp": get_timestamp()
    },
    "Weasley": {
        "first_name": "Ronald",
        "last_name": "Weasley",
        "timestamp": get_timestamp()
    },
    "Granger": {
        "first_name": "Hermione",
        "last_name": "Granger",
        "timestamp": get_timestamp()
    }
}

def read_all():
    return list(PEOPLE.values())

def create(person):
    last_name = person.get("last_name")
    first_name = person.get("first_name", "")

    if last_name and last_name not in PEOPLE:
        PEOPLE[last_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "timestamp": get_timestamp()
        }

        return PEOPLE[last_name], 201
    else:
        abort(
            406,
            f"Person with last name {last_name} already exists"
        )

def read_one(last_name):
    if last_name in PEOPLE:
        return PEOPLE[last_name]
    else:
        abort(
            404,
            f"Person with last name {last_name} not found   "
        )