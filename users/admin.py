from django.contrib import admin

from .models import Cart, Customer, ProductReviews

# Register your models here.
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(ProductReviews)