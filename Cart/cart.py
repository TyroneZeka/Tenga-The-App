from decimal import Decimal

from Base import settings
from Checkout.models import DeliveryOptions
from Products import models as productModels


class Cart:
    """
    A base Cart class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("skey")
        if "skey" not in request.session:
            cart = self.session["skey"] = {}
        self.cart = cart

    def add(self, product_meta, product_quantity):
        """
        Adding and updating products in cart session data
        """
        # TODO: Get ProductMeta from product_sku, color, and size
        #
        media = (
            productModels.Media.objects.filter(product=product_meta.product)
            .filter(is_feature=True)
            .first()
        )
        # print(product.media_product.filter(is_feature=True))
        product_sku = product_meta.sku
        if product_sku in self.cart:
            self.cart[product_sku]["quantity"] = int(product_quantity)
        else:
            # adding product attributes to cart, you choose what you want to add
            self.cart[product_sku] = {
                "name": str(product_meta.product),
                "price": str(product_meta.store_price),
                "quantity": int(product_quantity),
                "image": str(media.image),
            }

        self.save()

    def delete(self, product):
        """
        Delete the product from session data
        """
        product_sku = product.sku
        if product_sku in self.cart:
            del self.cart[product_sku]
        self.save()

    def update(self, product, quantity):
        product_sku = product.sku
        if product_sku in self.cart:
            self.cart[product_sku]["quantity"] = int(quantity)

        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        """
        To make the session data iterable.
        Collect the product ids and make query of product details return products
        """
        product_skus = self.cart.keys()
        products = productModels.ProductMeta.objects.filter(
            sku__in=product_skus
        )

        cart = self.cart.copy()

        for product in products:
            cart[str(product.sku)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            item["image"] = settings.MEDIA_URL + item["image"]

            yield item

    def __len__(self):
        """
        Get the cart dart and count the quantity in cart
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_subtotal_price(self):
        """
        To get the sub_ total of the cart
        """
        return sum(
            Decimal(item["price"]) * int(item["quantity"])
            for item in self.cart.values()
        )

    def get_delivery_price(self):
        newprice = 0.00

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(
                id=self.session["purchase"]["delivery_id"]
            ).delivery_price

        return newprice

    def get_total_price(self):
        newprice = 0.00
        subtotal = sum(
            Decimal(item["price"]) * item["quantity"]
            for item in self.cart.values()
        )
        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(
                id=self.session["purchase"]["delivery_id"]
            ).delivery_price

        total = subtotal + Decimal(newprice)
        return total

    def cart_update_delivery(self, deliveryprice=0):
        subtotal = sum(
            Decimal(item["price"]) * item["quantity"]
            for item in self.cart.values()
        )
        total = subtotal + Decimal(deliveryprice)
        return total

    def clear(self):
        # Remove cart from session
        del self.session[settings.CART_SESSION_ID]
        del self.session["address"]
        del self.session["purchase"]
        self.save()
