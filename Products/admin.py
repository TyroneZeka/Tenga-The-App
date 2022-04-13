from dataclasses import fields
from django.contrib import admin
from .models import Category, Product, ProductMeta
from users.models import Customer
from django import forms

# Register your models here.
# customer = Customer.objects.get(username='mufasa')
"""I can do all admin functionalities in this file and also get model data"""

# Admin dashboard
class ProductsAdminArea(admin.AdminSite):
    site_header = "Tenga Online Shopping System Admin"
    # site_header = customer.username

products_admin_site = ProductsAdminArea(name="TOSS Admin")


class ProductForm(forms.BaseModelForm):
    def __init__(self, *args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        self.fields['name'].help_text = 'My Help Text'

    class Meta:
        model = Product
        exclude = ('',)

# for product filtering
class ProductsAdmin(admin.ModelAdmin):
    fields = ['name','description','category','is_active']
    list_display = ("name","product_category")


class ProductMetaAdmin(admin.ModelAdmin):
    list_display = ['product','product_type','Brand','Attributes']







products_admin_site.register(Product,ProductsAdmin)
products_admin_site.register(Category)
products_admin_site.register(ProductMeta,ProductMetaAdmin)