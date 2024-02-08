from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def catalog(request: HttpRequest) -> HttpResponse:
    return render(request, "goods/catalog.html")


def product(request: HttpRequest) -> HttpResponse:
    return render(request, "goods/product.html")
