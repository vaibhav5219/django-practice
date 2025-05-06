from django.db import models

class News(models.Model):
    title = models.CharField(max_length=1000)
    description =models.TextField()
    image = models.URLField()
    external_link = models.URLField()
    
class Info(models.Model):
    info = models.CharField(max_length=100)