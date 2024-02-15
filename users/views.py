from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


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
                messages.success(request, f"{cd["username"]} you are logged in")
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
            messages.success(request, f"{user.username} you have "
                                      "successfully registered and "
                                      "logged into your account")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()
    context = {"title": "Home - Registration", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)
    context = {"title": "Home - Profile", "form": form}
    return render(request, "users/profile.html", context)


@login_required
def logout(request: HttpRequest) -> HttpResponse:
    messages.success(request, f"{request.user.username} you have been logged")
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index"))
