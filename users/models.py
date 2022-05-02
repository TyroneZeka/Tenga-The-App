import uuid

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from Products.models import ProductMeta


# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(
        max_length=200, unique=True, null=True, blank=True
    )
    profilePicture = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("user image"),
        upload_to="images/profiles/",
        default="images/profiles/user-default.png",
        help_text=_("format: required, default-default.png"),
    )
    email = models.EmailField(max_length=500, blank=False, null=False)
    phone = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            "l@1.com",
            [self.email],
            fail_silently=False,
        )

    def __str__(self) -> str:
        return str(self.firstName)


class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    address1 = models.CharField(max_length=250, blank=True, null=True)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    post_code = models.CharField(max_length=25, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customer_address",
    )
    default = models.BooleanField(_("Default"), default=False)

    def __str__(self) -> str:
        return str(self.id)


class Cart(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True
    )
    products = models.ForeignKey(
        ProductMeta,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("Products in Cart"),
    )

    class Meta:
        verbose_name = str("Cart")
        verbose_name_plural = "Carts"

    def __str__(self):
        return str(self.customer.username)

    # Get More Info on get_absolute_url
    # def get_absolute_url(self):
    #     return reverse("Cart_detail", kwargs={"pk": self.pk})


class ProductReviews(models.Model):
    """
    Reviews for the products in shop
    """

    product = models.ForeignKey(ProductMeta, on_delete=models.PROTECT)
    customer = models.ForeignKey(
        Customer, related_name="customer", on_delete=models.PROTECT
    )
    review = models.TextField(
        max_length=500,
        unique=False,
        blank=False,
        null=False,
        editable=True,
    )

    def __str__(self):
        return str(self.customer.username)
