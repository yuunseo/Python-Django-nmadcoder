from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "name",
            "pk",
            "country",
            "price",
            "city",
        )
        depth = 1


class RoomDetailSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1
