from django.db import models
from common.models import CommonModel


# Create your models here.
class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    experiences = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )

    rooms = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    # room과 experience 한 가지만 했을 경우를 고려해, null과 blank 추가

    payload = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} / ⭐{self.rating}"
