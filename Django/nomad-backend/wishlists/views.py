from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from rest_framework.response import Response
from .serializers import WishlistSerializer
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from rooms.models import Room


class WishLists(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(
            user=request.user,
        )
        serializer = WishlistSerializer(
            all_wishlists,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(
                user=request.user,
            )
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WishListDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Wishlist.objects.get(
                pk=pk,
                user=user,
            )
        except Wishlist.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        one_wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(
            one_wishlist,
            context={"request": request},
        )
        return Response(serializer.data)

    def delete(self, request, pk):
        one_wishlist = self.get_object(pk, request.user)
        one_wishlist.delete()
        serializer = WishlistSerializer(one_wishlist)
        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        one_wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(
            one_wishlist,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            new = serializer.save()
            serializer = WishlistSerializer(new)
            return Response(serializer.data)
        else:
            raise Response(serializer.errors)


class WishlistToggle(APIView):
    permission_classes = [IsAuthenticated]

    def get_list(self, pk, user):
        try:
            return Wishlist.objects.get(
                pk=pk,
                user=user,
            )
        except Wishlist.DoesNotExist:
            raise NotFound

    def get_room(self, pk):
        try:
            return Room.objects.get(
                pk=pk,
            )
        except Room.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        one_wishlist = self.get_list(pk, request.user)
        room = self.get_room(room_pk)
        if one_wishlist.rooms.filter(pk=room_pk).exists():
            one_wishlist.rooms.remove(room)
        else:
            one_wishlist.rooms.add(room)
        return Response(status=HTTP_200_OK)
