from django.contrib import admin
from Products.admin import products_admin_site

from .models import Order

# Register your models here.
products_admin_site.register(Order)
