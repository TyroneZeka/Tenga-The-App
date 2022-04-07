from django.shortcuts import render

# Create your views here.

# Create your views here.
def home(request):
    context = {}
    return render(request,'products/index.html',context)

def search(request):
    context = {}
    return render(request,'products/search.html',context)

def productDetails(request):
    return render(request,'products/product.html',{})

