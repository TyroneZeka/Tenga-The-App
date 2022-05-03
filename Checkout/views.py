import json

from Cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from Orders.models import Order, OrderItem
from paypalcheckoutsdk.orders import OrdersGetRequest
from users.models import Address, Customer

from Checkout.paypal import PayPalClient

from .models import DeliveryOptions


# Create your views here.
@login_required(login_url="users:login")
def deliverychoices(request):
    if not bool(request.session["cart"]):
        messages.success(request, "No Item in Cart!")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(
        request,
        "checkout/delivery_choices.html",
        {"deliveryoptions": deliveryoptions},
    )


@login_required(login_url="users:login")
def cart_update_delivery(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        delivery_option = int(request.POST.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = cart.cart_update_delivery(
            delivery_type.delivery_price
        )

        session = request.session
        if "purchase" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True

        response = JsonResponse(
            {
                "total": updated_total_price,
                "delivery_price": delivery_type.delivery_price,
            }
        )
        return response


@login_required(login_url="users:login")
def delivery_address(request):
    session = request.session
    if "purchase" not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    customer = Customer.objects.get(user=request.user)
    addresses = Address.objects.filter(customer_id=customer.id).order_by(
        "-default"
    )

    if "address" not in request.session:
        session["address"] = {"address_id": str(addresses[0].id)}
    else:
        session["address"]["address_id"] = str(addresses[0].id)
        session.modified = True

    return render(
        request, "checkout/delivery_address.html", {"addresses": addresses}
    )


@login_required
def payment_complete(request):
    PPClient = PayPalClient()

    body = json.loads(request.body)
    data = body["orderID"]
    customer = Customer.objects.get(user=request.user)
    requestorder = OrdersGetRequest(data)
    response = PPClient.client.execute(requestorder)
    print(response.result.purchase_units[0].shipping.name.full_name)
    cart = Cart(request)
    order = Order.objects.create(
        user=customer,
        full_name=response.result.purchase_units[0].shipping.name.full_name,
        email=response.result.payer.email_address,
        address1=response.result.purchase_units[
            0
        ].shipping.address.address_line_1,
        address2=response.result.purchase_units[
            0
        ].shipping.address.admin_area_2,
        postal_code=response.result.purchase_units[
            0
        ].shipping.address.postal_code,
        country_code=response.result.purchase_units[
            0
        ].shipping.address.country_code,
        total_paid=response.result.purchase_units[0].amount.value,
        order_key=response.result.id,
        payment_option="paypal",
        billing_status=True,
    )
    order_id = order.pk

    for item in cart:
        OrderItem.objects.create(
            order_id=order_id,
            product=item["product"],
            price=item["price"],
            quantity=item["quantity"],
        )

    return JsonResponse("Payment completed!", safe=False)


@login_required
def payment_successful(request):
    cart = Cart(request)
    cart.clear()
    return redirect("users:user_orders")
