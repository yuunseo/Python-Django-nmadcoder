from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


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
    owner = TinyUserSerializer()
    amenities = AmenitySerializer(many=True)
    categoryy = CategorySerializer()

    class Meta:
        model = Room
        fields = "__all__"
