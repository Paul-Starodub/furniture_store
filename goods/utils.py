from django.db.models import QuerySet

from goods.models import Products


def q_search(query: str) -> QuerySet:
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    return Products.objects.filter(description__search=query)
