from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users_images", blank=True, null=True, verbose_name="Avatar"
    )

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.username
