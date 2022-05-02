from django.contrib import admin
from Products.admin import products_admin_site

from .models import Address, Customer, ProductReviews

# Register your models here.
products_admin_site.register(Customer)
products_admin_site.register(Address)
products_admin_site.register(ProductReviews)
