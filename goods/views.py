from typing import Optional, Any

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from goods.models import Products
from goods.utils import q_search


def catalog(
    request: HttpRequest, category_slug: Optional[Any] = None
) -> HttpResponse:
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, per_page=3)
    current_page = paginator.page(int(page))
    context = {
        "title": "Home - Catalog",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request: HttpRequest, product_slug: str) -> HttpResponse:
    product = get_object_or_404(Products, slug=product_slug)
    context = {"product": product}
    return render(request, "goods/product.html", context=context)
