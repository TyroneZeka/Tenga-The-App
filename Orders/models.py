from ast import Or
from decimal import Decimal
from itertools import product

from django.conf import settings
from django.db import models
from Products import models as Productsmodels
from users import models as Usermodels

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        Usermodels.Customer,
        on_delete=models.CASCADE,
        related_name="order_user",
    )
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    address1 = models.CharField(max_length=250, null=True, blank=True)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country_code = models.CharField(max_length=4, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    payment_option = models.CharField(max_length=200, blank=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Productsmodels.ProductMeta,
        related_name="order_items",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)
