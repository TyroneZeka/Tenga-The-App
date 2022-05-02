from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Cart, Customer


@receiver(post_save, sender=User)
def createCustomer(sender, instance, created, **kwargs):
    if created:
        user = instance
        if not user.is_staff:
            customer = Customer.objects.create(
                user=user,
                username=user.username,
                firstName=user.first_name,
                lastName=user.last_name,
                email=user.email,
            )
            # implement send_mail for when a new customer reegisters.
            # TODO: if admin, no need for mail but only new customers.


@receiver(post_save, sender=Customer)
def updateCustomer(sender, instance, created, **kwargs):
    customer = instance
    user = customer.user

    if created == False:
        user.first_name = customer.firstName
        user.last_name = customer.lastName
        user.email = customer.email


@receiver(post_save, sender=Customer)
def createCustomerCart(sender, instance, created, **kwargs):
    customer = instance

    if created:
        cart = Cart.objects.create(customer=customer)


# I can go on and implement post_delete for when a customer wants to delete their account maybe to delete the account from the system.
