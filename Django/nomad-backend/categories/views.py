from django.shortcuts import render
from .models import Category
from django.http import JsonResponse


# Create your views here.
def categories(request):
    all_categories = Category.objects.all()
    # 우리는 user에게 HttpResponse를 전달하지 않을것.
    # 우리는 JSON을 전달할거야.
    return JsonResponse({"ok": True})
