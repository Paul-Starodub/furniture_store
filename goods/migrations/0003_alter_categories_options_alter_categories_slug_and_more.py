# Generated by Django 4.2.8 on 2024-02-09 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0002_alter_categories_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categories",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.AlterField(
            model_name="categories",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=200, null=True, unique=True, verbose_name="URL"
            ),
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="goods_images"),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
                ),
                (
                    "discount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
                ),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="goods.categories",
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
                "db_table": "product",
            },
        ),
    ]