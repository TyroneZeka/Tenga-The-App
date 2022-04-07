from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cart, Customer
from django.conf import settings

@receiver(post_save,sender=User)
def createCustomer(sender,instance,created,**kwargs):
    if created:
        user = instance
        customer = Customer.objects.create(
            user = user,
            username = user.username,
            firstName = user.first_name,
            lastName = user.last_name,
            email = user.email,
        )
    print('createCustomer function run!!')
        # implement send_mail for when a new customer reegisters. 
        # TODO: if admin, no need for mail but only new customers.

@receiver(post_save,sender=Customer)
def updateCustomer(sender,instance,created,**kwargs):
    customer = instance
    user = customer.user

    if created == False:
        user.first_name = customer.firstName
        user.last_name = customer.lastName
        user.email = customer.email
    print('updateCustomer func run!!!')

@receiver(post_save,sender = Customer)
def createCustomerCart(sender,instance,created,**kwargs):
    customer = instance

    if created:
        cart = Cart.objects.create(
            customer = customer
        )


# I can go on and implement post_delete for when a customer wants to delete their account maybe to delete the account from the system.