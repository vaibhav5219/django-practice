from django.db import models # type: ignore
from django.contrib.auth.models import AbstractBaseUser # type: ignore
from accounts.managers import UserManager

class CustomUser(AbstractBaseUser):
    username = None
    phone_number = models.CharField(max_length=12, unique=True)
    profile_image= models.ImageField(upload_to="profile", null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    otp = models.IntegerField(default=0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
