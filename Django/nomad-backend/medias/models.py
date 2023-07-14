from django.db import models
from common.models import CommonModel


# Create your models here.
class Photo(CommonModel):

    """Media(Photo) Model Definition"""

    file = models.ImageField()
    description = models.TextField()
    rooms = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experiences = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    """Media(Video) Model Definition"""

    file = models.FileField()
    experiences = models.OneToOneField(
        "experiences.Experience", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Video File"
