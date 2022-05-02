from django import forms
from django.contrib import admin

from . import models

# Register your models here.
# customer = Customer.objects.get(username='mufasa')
"""I can do all admin functionalities in this file and also get model data"""

# Admin dashboard
class ProductsAdminArea(admin.AdminSite):
    site_header = "TOSS Admin"
    # site_header = customer.username


products_admin_site = ProductsAdminArea(name="TOSS Admin")


class ProductForm(forms.BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].help_text = "My Help Text"

    class Meta:
        model = models.Product
        exclude = ("",)


# for product filtering
class ProductsAdmin(admin.ModelAdmin):
    fields = ["name", "description", "category", "is_active"]
    list_display = ("name", "product_category")


class ProductMetaAdmin(admin.ModelAdmin):
    list_display = ["product", "product_type", "Brand", "Attributes"]


# admin.site.register(models.Product)
# admin.site.register(models.Media)
# admin.site.register(models.Category)
# admin.site.register(models.ProductMeta)

products_admin_site.register(models.Product, ProductsAdmin)
products_admin_site.register(models.Media)
products_admin_site.register(models.Category)
products_admin_site.register(models.ProductMeta, ProductMetaAdmin)
