from rest_framework.urls import path
from .views import WishLists

urlpatterns = [
    path("", WishLists.as_view()),
]
