from django.shortcuts import render
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer


# Create your views here.
@api_view()
def categories(request):
    all_cate = Category.objects.all()
    serializer = CategorySerializer(all_cate, many=True)
    return Response(
        {
            "ok": True,
            "categoris": serializer.data,
        }
    )
