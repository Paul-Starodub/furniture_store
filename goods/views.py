from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from goods.models import Products


def catalog(request: HttpRequest) -> HttpResponse:
    goods = Products.objects.all()
    context = {"title": "Home - Catalog", "goods": goods}
    return render(request, "goods/catalog.html", context=context)


def product(request: HttpRequest, product_slug: str) -> HttpResponse:
    product = get_object_or_404(Products, slug=product_slug)
    context = {"product": product}
    return render(request, "goods/product.html", context=context)
