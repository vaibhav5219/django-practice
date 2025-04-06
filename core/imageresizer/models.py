from django.db import models
from django.db.models.signals import (pre_init, pre_delete, pre_save, pre_migrate,
                                      post_delete, post_init, post_migrate, post_save)
from django.dispatch import receiver
from PIL import Image
import os

class Student(models.Model):
    student_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=100, choices=(('Male', 'Male'), ('Female','Female')))
    student_id = models.CharField(max_length=10, null=True, blank=True)
    

@receiver(post_save, sender=Student)
def save_student(sender, instance,created, **kwargs):
    print(sender)
    print(instance)
    if created:
        instance.student_id = f"STU-000{instance.id}"
        instance.save()
        print("Student Object Created at first time")
    else:
        print("Student object updated")
        
@receiver(pre_delete, sender=Student)
def delete_student(sender, instance, **kwargs):
    print("object deleted")

    
    
''' Image model '''
class ImageModel(models.Model):
    original_image = models.ImageField(upload_to="images/")
    thumbnail_small = models.ImageField(upload_to="images/thumbnaila", null=True, blank=True)
    thumbnail_medium = models.ImageField(upload_to="images/thumbnaila", null=True, blank=True)
    thumbnail_large = models.ImageField(upload_to="images/thumbnaila", null=True, blank=True)
    
    class Meta:
        db_table = "imagemodel"
    
@receiver(post_save, sender=ImageModel)
def create_thumbnails(sender, instance, created, **kwargs):
    if created:
        sizes = {
            "thumbnail_small" : (100, 100),
            "thumbnail_medium" : (300, 300),
            "thumbnail_large" : (600, 600),
        }
        
        for fields, size in sizes.items():
            img = Image.open(instance.original_image.path)
            img.thumbnail(size, Image.Resampling.LANCZOS)
            thumb_name, thumb_extension = os.path.split(instance.original_image.name)
            thumb_extension = thumb_extension.lower()
            thumb_filename = f"{thumb_name}_{size[0]}x{size[1]}{thumb_extension}"
            thumb_path = f"thumbnails/{thumb_filename}"
            img.save(thumb_path)
            setattr(instance, fields, thumb_path)