from django.urls import path
from goods import views

urlpatterns = [
    path("<slug:category_slug>/", views.catalog, name="index"),
    path(
        "<slug:category_slug>/<int:page>/", views.catalog, name="index"
    ),  # not good practice
    path("product/<slug:product_slug>/", views.product, name="product"),
]

app_name = "catalog"
