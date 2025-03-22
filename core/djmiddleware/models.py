from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Store(models.Model):
    bmp_id = models.CharField(unique=True, max_length=100)
    store_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self): # type: ignore
        return self.store_name
