from django.db import models
from django.contrib.auth.models import AbstractUser

from users.utils import CustomUserManager

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_professor = models.BooleanField()
    updated_at = models.TimeField(null=True)
    img = models.URLField(null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "is_professor"]
    objects = CustomUserManager()
