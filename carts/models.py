from decimal import Decimal

from django.db import models

from goods.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self) -> int:
        return sum(cart.product_price() for cart in self)

    def total_quantity(self) -> int:
        if self:
            return sum(cart.quantity for cart in self)

        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="customer",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="product"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="date added"
    )

    objects = CartQueryset.as_manager()

    def __str__(self) -> str:
        return f"Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}"

    def product_price(self) -> Decimal:
        return round(self.product.sell_price() * self.quantity, 2)
