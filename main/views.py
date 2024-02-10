from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request: HttpRequest) -> HttpResponse:
    categories = Categories.objects.all()
    context = {
        "title": "Home - Main Page",
        "content": "FURNITURE STORE HOME",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home - About us",
        "content": "About us",
        "text_on_page": "About this cool store",
    }
    return render(request, "main/about.html", context)
