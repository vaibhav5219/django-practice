from django.shortcuts import render
from rabbit_mq_app.rabbit_mq_script import publish_message
import random
from faker import Faker # type: ignore
fake = Faker()


def index(request):
    message = f"This is a demo message {random.randint(0, 10)}"
    # publish_message(message)
    names = [
        {"name": fake.name(), "address": fake.address()} for _ in range(10)
    ]
    publish_message(names)

    return render(request, 'index.html')