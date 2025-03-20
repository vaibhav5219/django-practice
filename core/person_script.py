import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","core.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"
django.setup()
from datetime import datetime, timedelta
from django.db.models import Avg, Count, Min, Max, Count, Sum, Q, Subquery, OuterRef
import random
from home.models import Person, Skills
from faker import Faker

fake = Faker()


def bulk_create_person(number):
    bulk_create_list = []
    bulk_create_list = [ Person(person_name = fake.name()) for _ in range(number) ]
    # print(bulk_create_list)

    # Person.objects.bulk_create(bulk_create_list) # bulk create
    # Person.objects.all().delete() # bulk delete
    print(Person.objects.filter(person_name__icontains = 'Devis').count())
    Person.objects.filter(person_name__icontains = 'Dev').update(person_name = "Sharma") # bulk update


bulk_create_person(1000)
