from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from users.utils import CustomUserManager

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_professor = models.BooleanField()
    updated_at = models.TimeField(null=True)
    img = models.URLField(null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "is_professor"]
    objects = CustomUserManager()
