from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def login(request: HttpRequest) -> HttpResponse:
    context = {"title": "Home - Authorization"}
    return render(request, "users/login.html", context)


def registration(request: HttpRequest) -> HttpResponse:
    context = {"title": "Home - Registration"}
    return render(request, "users/registration.html", context)


def profile(request: HttpRequest) -> HttpResponse:
    context = {"title": "Home - Profile"}
    return render(request, "users/profile.html", context)


def logout(request: HttpRequest) -> HttpResponse:
    pass
