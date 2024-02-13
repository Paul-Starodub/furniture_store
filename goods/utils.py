from django.contrib.postgres.search import SearchVector
from django.db.models import QuerySet

from goods.models import Products


def q_search(query: str) -> QuerySet:
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    return Products.objects.annotate(
        search=SearchVector("name", "description")
    ).filter(search=query)
