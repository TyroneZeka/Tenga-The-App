from django.contrib import admin
from Products.admin import products_admin_site

from .models import DeliveryOptions

# Register your models here.
products_admin_site.register(DeliveryOptions)
