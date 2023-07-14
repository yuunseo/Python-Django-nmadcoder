from typing import Any, Optional
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class GoodBadFilter(admin.SimpleListFilter):
    title = "Filter by Good or Bad!"
    parameter_name = "standard"

    def lookups(self, request, model_admin):
        return [
            ("good_review", "Good Review"),
            ("bad_review", "Bad Review"),
        ]

    def queryset(self, request, reviews):
        std = self.value()
        if std:
            if std == "bad_review":
                return reviews.filter(rating__lt=3)
            else:
                return reviews.filter(rating__gte=3)
        else:
            reviews


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        GoodBadFilter,
        "rating",
        "user__is_host",
        "rooms__categoryy",
    )
