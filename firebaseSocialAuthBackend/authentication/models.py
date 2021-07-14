from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Class for creating models for users.
    """
    name = models.CharField(max_length=50, null=True, blank=False)
    uid = models.CharField(max_length=150, null=True)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': 'This email address is already associated with another account.'})
    image = models.URLField(null=True, blank=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        """
        Function to return email.
        """
        return self.email
