from django.db import models
import uuid

# Create your models here.


class TimesChoices(models.TextChoices):
    MANHA700 = ("07:00:00", "7H00")
    MANHA750 = ("07:50:00", "7H50")
    MANHA840 = ("08:40:00", "8H40")
    MANHA930 = ("09:30:00", "9H30")
    MANHA950 = ("09:50:00", "9H50")
    MANHA1040 = ("10:40:00", "10H40")
    MANHA1130 = ("11:30:00", "11H30")
    MANHA1220 = ("12:20:00", "12H20")
    TARDE1320 = ("13:20:00", "12H20")
    TARDE1410 = ("14:10:00", "14H10")
    TARDE1500 = ("15:00:00", "15H00")
    TARDE1550 = ("15:50:00", "15H50")
    TARDE1610 = ("16:10:00", "16H10")
    TARDE1700 = ("17:00:00", "17H00")
    TARDE1750 = ("17:50:00", "17H50")
    TARDE1840 = ("18:40:00", "18H40")
    NOITE1810 = ("18:10:00", "18H10")
    NOITE1900 = ("19:00:00", "19H00")
    NOITE1950 = ("19:50:00", "19H50")
    NOITE2040 = ("20:40:00", "20H40")
    NOITE2050 = ("20:50:00", "20H50")
    NOITE2140 = ("21:40:00", "21H40")
    NOITE2230 = ("22:30:00", "22H30")


class Scheduling(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user"
    )
    scheduling_date_start = models.DateField(default="2020-02-22")
    scheduling_date_end = models.DateField()
    scheduling_time_start = models.TimeField(
        choices=TimesChoices.choices, default=TimesChoices.MANHA700
    )
    scheduling_time_end = models.TimeField(
        choices=TimesChoices.choices, default=TimesChoices.MANHA750
    )
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=255, default="")
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="room"
    )
