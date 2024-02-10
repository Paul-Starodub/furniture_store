from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from goods.models import Products


def catalog(request: HttpRequest) -> HttpResponse:
    goods = Products.objects.all()
    context = {"title": "Home - Catalog", "goods": goods}
    return render(request, "goods/catalog.html", context=context)


def product(request: HttpRequest) -> HttpResponse:
    return render(request, "goods/product.html")
