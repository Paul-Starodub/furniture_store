from django import template
from django.db.models import QuerySet
from django.http import HttpRequest

from carts.models import Cart

register = template.Library()


@register.simple_tag()
def user_carts(request: HttpRequest) -> QuerySet:
    return Cart.objects.filter(user=request.user)
