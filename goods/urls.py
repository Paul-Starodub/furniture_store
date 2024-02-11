from django.urls import path
from goods import views

urlpatterns = [
    path("", views.catalog, name="index"),
    path("product/<int:product_id>/", views.product, name="product"),
]

app_name = "catalog"
