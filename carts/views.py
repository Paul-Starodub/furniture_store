from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from carts.models import Cart
from goods.models import Products


def cart_add(request: HttpRequest, product_slug: str):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def cart_change(request, product_slug):
    pass


def cart_remove(request, product_slug):
    pass
