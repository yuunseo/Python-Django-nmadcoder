from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Amenity
from .serializers import AmenitySerializer


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = (
                serializer.save()
            )  # .save()이후 장고는 new data가 저장된 amenities in new DB 반환
            return Response(
                AmenitySerializer(amenity).data
            )  # 새롭게 업데이트 된 정보를 다시 JSON으로 내보내고 있다.
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
