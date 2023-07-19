from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from rest_framework.serializers import SerializerMethodField


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    rating_avg = SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "name",
            "rating_avg",
            "pk",
            "country",
            "price",
            "city",
        )
        depth = 1

    def get_rating_avg(self, room):
        return room.rating()


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(
        many=True,
        read_only=True,
    )
    categoryy = CategorySerializer(
        read_only=True,
    )
    rating_avg = SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating_avg(self, room):
        return room.rating()
