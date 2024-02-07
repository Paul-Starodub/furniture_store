from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Home Page")


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About")
