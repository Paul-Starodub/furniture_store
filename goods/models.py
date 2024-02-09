from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"
