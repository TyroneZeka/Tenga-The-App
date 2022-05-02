from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.homeView, name="home-view"),
    path(
        "product/<str:slug>/",
        views.singleProductView,
        name="single-product-view",
    ),
    path("search/", views.search, name="search-view"),
]
