from .models import News

def my_scheduled_job():
    News.objects.create(
        title = "Title 1",
        description = "Description 2",
        image = "https://pypi.org/project/django-crontab/",
        external_link = "https://www.codementor.io/@akul08/the-ultimate-crontab-cheatsheet-5op0f7o4r",
    )
    