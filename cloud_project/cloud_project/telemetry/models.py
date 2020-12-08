from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager

# Create your models here.
class App_users(AbstractUser):
    username = None
    name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email

	