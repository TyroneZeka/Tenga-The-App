from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.productDetails,name='productDetails'),
    path('search/',views.search,name='search'),
    
]