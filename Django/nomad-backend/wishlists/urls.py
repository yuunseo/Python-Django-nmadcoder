from rest_framework.urls import path
from .views import WishLists, WishListDetail, WishlistToggle

urlpatterns = [
    path("", WishLists.as_view()),
    path("<int:pk>", WishListDetail.as_view()),
    path("<int:pk>/rooms/<int:room_pk>", WishlistToggle.as_view()),
]
