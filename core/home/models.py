from django.db import models
from django.template.defaultfilters import slugify
from home.utils import *

class College(models.Model):
    College_name = models.CharField(max_length = 255)
    college_address = models.CharField(max_length=255)


# Create your models here.
class Students(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=10, choices=gender_choices, null=True, blank=True)
    college = models.ForeignKey(College, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    file = models.FileField()
    student_bio = models.TextField(null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)

class Car(models.Model):
    def __str__(self):
        return self.car_name + ' -> ' + str(self.speed)

    car_name = models.CharField(max_length=255)
    speed = models.IntegerField(default=20)


class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(default='IN', max_length=100)

    def __str__(self):
        return self.brand_name
    
class SkillsManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted=False)
    
class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.id: # type: ignore
            self.slug = generateSlug(self.product_name, Product) # should not call in case of update
        print("product Save Called, slug => ", self.slug)
        return super().save(*args, **kwargs)

class Skills(models.Model):
    skill_name = models.CharField(max_length=255)
    is_soft_skill = models.BooleanField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = SkillsManager()
    new_manager = models.Manager()
    
    def __str__(self):
        return self.skill_name
    
    class Meta:
        db_table = "skills"
        unique_together = ('skill_name', 'is_soft_skill',)
        index_together = ('skill_name', 'is_soft_skill',)


class Person(models.Model):
    person_name = models.CharField(max_length=255)
    skill = models.ManyToManyField(Skills)

    class Meta:
        db_table = "person"
        ordering = ['person_name']
        verbose_name = "Persones"  # will used for admin panel
        verbose_name_plural = "Persones" # will used for admin panel

class Human(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)

    class Meta:
        abstract = True  # make as a base class

class Employee(Human):
    Address = models.CharField(max_length=255)
    
    class Meta: # type: ignore
        permissions = ("can_do_something", "Can do something"),