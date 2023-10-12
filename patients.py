from datetime import datetime
from flask import abort
from faker import Faker
from faker.providers import date_time
import uuid
import random

fake = Faker()
fake.add_provider(date_time)


def get_all():
    patients = []
    random_num_grantors = random.randint(0, 15)
    if random_num_grantors == 0:
        return patients
    for _ in range(random_num_grantors):
        patients.append(
            {
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "patientId": uuid.uuid4(),
                "birthDate": fake.date_of_birth(minimum_age=18, maximum_age=115),
            }
        )
    return patients
