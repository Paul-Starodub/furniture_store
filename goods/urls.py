from django.urls import path
from goods import views

urlpatterns = [
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]

app_name = "catalog"
