from tkinter import CASCADE
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid 

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True, blank= True)
    firstName = models.CharField(max_length=100, null=True,blank=True)
    lastName = models.CharField(max_length=100, null = True, blank = True)
    username = models.CharField(max_length=200,unique=True, null = True, blank = True)
    profilePicture = models.ImageField(null = True,blank = True,verbose_name=_("user image"), upload_to = 'images/profiles/', default = 'images/profiles/user-default.png', help_text=_("format: required, default-default.png"))
    email = models.EmailField(max_length = 500,blank= False,null= False)
    phone = models.IntegerField(null = True, blank = True)
    bio = models.TextField(blank=True,null = True)

    def __str__(self) -> str:
        return str(self.firstName)


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    address = models.CharField(max_length=500,blank=True,null=True)
    city = models.CharField(max_length=100, null = True,blank = True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.address)


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null = True, blank = True)
    # products = models.ForeignKey(ProductMeta,)

    class Meta:
        verbose_name = str("Cart")
        verbose_name_plural = ("Carts")

    def __str__(self):
        return self.customer.id
    
    # Get More Info on get_absolute_url
    # def get_absolute_url(self):
    #     return reverse("Cart_detail", kwargs={"pk": self.pk})


