from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class ShopAdminConfig(AdminConfig):
    default_site = 'Products.admin.ProductsAdminArea'

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Products'
