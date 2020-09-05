from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom User manager where email is the unique identifier for 
    authentication instead of  username"""
    def create_user(self, email, password, **extra_fields):
        """Create and save a user with the given username and
        password"""
        if not email:
            raise ValueError(_("A valid email is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        """Create and save a superuser using the email & password"""
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff set to True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser set to True"))

        return self.create_user(email, password, **extra_fields)
