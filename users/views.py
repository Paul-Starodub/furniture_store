from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def login(request: HttpRequest) -> HttpResponse:
    context = {"title": "Home - Authorization"}
    return render(request, "", context)


def registration(request: HttpRequest) -> HttpResponse:
    context = {"title": "Home - Registration"}
    return render(request, "", context)


def profile(request: HttpRequest) -> HttpResponse:
    context = {"title": "Home - Profile"}
    return render(request, "", context)


def logout(request: HttpRequest) -> HttpResponse:
    pass
