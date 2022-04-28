from django.urls import path

from . import views

urlpatterns = [
    path("", views.homeView, name="home-view"),
    path(
        "product/<str:slug>/",
        views.singleProductView,
        name="single-product-view",
    ),
    path("search/", views.search, name="search-view"),
]
