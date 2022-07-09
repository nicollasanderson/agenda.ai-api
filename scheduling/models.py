from django.db import models
from datetime import time

# Create your models here.

class Scheduling(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user')
    scheduling_date = models.DateField()
    scheduling_start = models.TimeField()
    scheduling_end = models.TimeField()
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE, related_name='room')