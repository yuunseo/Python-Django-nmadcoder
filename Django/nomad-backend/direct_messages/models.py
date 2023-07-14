from django.db import models
from common.models import CommonModel


# Create your models here.
class ChattingRoom(CommonModel):
    users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return f"Chatting Room"


class Message(CommonModel):
    text = models.TextField()
    users = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    rooms = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.users} says: {self.text}"
