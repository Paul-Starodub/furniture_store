from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home",
        "content": "Welcome to Home",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "is_authenticated": True,
    }
    return render(request, "main/index.html", context)


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About")
