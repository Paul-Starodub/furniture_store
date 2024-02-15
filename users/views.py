from django.contrib import auth
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()
    context = {"title": "Home - Authorization", "form": form}
    return render(request, "users/login.html", context)


def registration(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()
    context = {"title": "Home - Registration", "form": form}
    return render(request, "users/registration.html", context)


def profile(request: HttpRequest) -> HttpResponse:
    context = {"title": "Home - Profile"}
    return render(request, "users/profile.html", context)


def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index"))
