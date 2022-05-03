from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from Products import models as productModels

from .cart import Cart


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    return render(request, "cart/cart.html", {"cart": cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        product_color = str(request.POST.get("product_color"))
        product_size = int(request.POST.get("product_size"))
        product_meta = (
            productModels.ProductMeta.objects.filter(product__id=product_id)
            .filter(attribute_values__attribute_value=product_color)
            .filter(attribute_values__attribute_value=product_size)
        ).first()
        cart.add(product_meta=product_meta, product_quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({"quantity": cart_quantity})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "delete":
        product_sku = request.POST.get("product_meta")
        product = get_object_or_404(productModels.ProductMeta, sku=product_sku)
        cart.delete(product)
        cart_quantity = cart.__len__()
        total = cart.get_total_price()
        response = JsonResponse(
            {
                "Success": True,
                "quantity": cart_quantity,
                "total": total,
            }
        )
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get("action") == "update":
        product_sku = request.POST.get("product_sku")
        product_quantity = request.POST.get("product_quantity")
        product = get_object_or_404(productModels.ProductMeta, sku=product_sku)
        cart.update(product, product_quantity)
        cart_quantity = cart.__len__()
        total = cart.get_subtotal_price()
        # print(total)
        response = JsonResponse(
            {
                "Success": True,
                "quantity": cart_quantity,
                "total": total,
            }
        )
        return response
