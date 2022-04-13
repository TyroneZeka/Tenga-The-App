from django.shortcuts import render
from .models import ProductMeta

# Create your views here.

# Create your views here.
def home(request):
    context = {}
    # bestselling, you choose the first 50 products
    # shirts, you query other objects
    # shoes, you query a brand 
    return render(request,'products/index.html',context)

def search(request):
    context = {}
    return render(request,'products/search.html',context)

def product(request,pk):
    productObj = ProductMeta.objects.get(id=pk)
    for att in productObj.product_type.product_type_attribute.all():
        print(att)

    return render(request,'products/product.html',{'product': productObj})

