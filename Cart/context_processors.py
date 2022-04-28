from .cart import Cart


def cart(request):
    return {"cart": Cart(request)}


# You can add the price here to display on the cart
