from django.db import models
from common.models import CommonModel


# Create your models here.
class Booking(CommonModel):
    """Booking Model Definition"""

    class KindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=KindChoices.choices,
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    experiences = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    check_in = models.DateField()
    check_out = models.DateField()
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.kind} / {self.user}"
