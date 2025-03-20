from .models import *
from faker import Faker
import random
faker = Faker('en_IN')


def dbSeeder(records = 10) -> None:
    colleges = College.objects.all()

    for i in range(records):
        college_index = random.randint(0, colleges.count()-1)
        college = colleges[college_index]
        name = faker.name()
        gender_choice = random.choice(['Male', 'Female'])
        age = random.randint(18, 28)
        email = faker.email()
        address = faker.address()
        student_bio = faker.text()
        mobile_number = faker.phone_number()
    
        Students.objects.create(
            college = college,
            name = name,
            age = age,
            email = email,
            address = address,
            student_bio = student_bio,
            mobile_number = mobile_number,
            gender = gender_choice
        )

    # try:

    #     college_names_1 = ['LPU', 'Chandigadh University', 'NIT Patna', 'IIT Patna', 'RGPV', 'OIST', 'OCT', 'BITS Pilani', 'IIT Madras',
    #                     'BHU']
    #     for i in college_names_1:
    #         address = faker.address()
    #         College.objects.create(
    #             College_name = i,
    #             college_address = address
    #         )
    # except Exception as e:
    #     print(e)
