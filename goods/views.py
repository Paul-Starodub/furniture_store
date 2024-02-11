from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from goods.models import Products


def catalog(request: HttpRequest, category_slug: str) -> HttpResponse:
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )
    context = {"title": "Home - Catalog", "goods": goods}
    return render(request, "goods/catalog.html", context=context)


def product(request: HttpRequest, product_slug: str) -> HttpResponse:
    product = get_object_or_404(Products, slug=product_slug)
    context = {"product": product}
    return render(request, "goods/product.html", context=context)
