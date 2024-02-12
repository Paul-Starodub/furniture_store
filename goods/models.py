from decimal import Decimal

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

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", null=True, blank=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2
    )
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="categories"
    )

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.name} Quantity - {self.quantity}"

    def display_id(self) -> str:
        return f"{self.id:05}"

    def sell_price(self) -> Decimal:
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
