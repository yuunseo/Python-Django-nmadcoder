from rest_framework.urls import path
from .views import WishLists, WishListDetail

urlpatterns = [
    path("", WishLists.as_view()),
    path("<int:pk>", WishListDetail.as_view()),
]
