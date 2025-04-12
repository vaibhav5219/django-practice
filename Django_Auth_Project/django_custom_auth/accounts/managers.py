from django.contrib.auth.base_user import BaseUserManager  # type: ignore

class UserManager(BaseUserManager):
    
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")
        if not password:
            raise ValueError("Password is required")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if not extra_fields.setdefault('is_staff', True):
            raise ValueError("Super user must have is_staff=True")
        
        if not extra_fields.setdefault('is_superuser', True):
            raise ValueError("Super user must have is_superuser=True")
        
        if not extra_fields.setdefault('is_active', True):
            raise ValueError("Super user must have is_active=True")
        
        return self.create_user(phone_number, password, **extra_fields)