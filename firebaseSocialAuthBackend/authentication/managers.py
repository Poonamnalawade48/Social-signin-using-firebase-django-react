"""
This file is used for creating custom user manager for the correspondent custom user.
"""
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Class for creating custom manager for managing custom user.
    """

    def create_user(self, email=None, name=None, password=None, image=None, role="USER",
                    status="ACTIVE", **extra_fields):
        """
        Function for creating user w.r.t custom user.
        """
        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.is_superuser = False
        user.is_active = True
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        """
        Function for creating super user.
        """
        user = self.create_user(
            email,
            name,
            password,
            role='ADMIN',
            status='ACTIVE'
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
