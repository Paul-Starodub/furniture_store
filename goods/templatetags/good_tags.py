from django.db.models import QuerySet
from django import template

from goods.models import Categories


register = template.Library()


@register.simple_tag
def tag_categories() -> QuerySet[Categories]:
    return Categories.objects.all()
