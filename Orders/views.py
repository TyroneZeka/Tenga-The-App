from Cart.cart import Cart
from django.http.response import JsonResponse
from django.shortcuts import render
from users.models import Customer

from Orders.models import Order, OrderItem


# Create your views here.
def add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        order_key = request.POST.get("order_key")
        user_id = request.user.id
        customer = Customer.objects.get(id=user_id)
        cart_total = cart.get_total_price()

        # check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user_id=customer.id,
                address=customer.customer_address,
                total_paid=cart_total,
                order_key=order_key,
            )
            order_id = order.pk

            for item in cart:
                OrderItem.objects.create(
                    order_id=order_id,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

        response = JsonResponse({"success": "Return something"})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
