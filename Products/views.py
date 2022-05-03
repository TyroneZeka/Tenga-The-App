from django.shortcuts import render

from . import models, utils

# Create your views here.

# Create your views here.
def homeView(request):
    page = "index"
    products, search_query = utils.searchProduct(request, "-product__id")
    recent_products, x = utils.searchProduct(request, "product__id")
    custom_range, recent_products = utils.paginateProducts(
        request, recent_products, 8
    )
    custom_range, products = utils.paginateProducts(request, products, 8)
    context = {
        "products": products,
        "recent_products": recent_products,
        "search_query": search_query,
        "custom_range": custom_range,
        "page": page,
    }

    return render(request, "products/index.html", context)


def search(request):
    page = "search"
    products, search_query = utils.searchProduct(
        request, "product__store_price"
    )
    custom_range, products = utils.paginateProducts(request, products, 20)
    context = {
        "products": products,
        "page": page,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "products/search.html", context)


def singleProductView(request, slug):
    product = (
        models.Product.objects.filter(slug__iexact=slug)
        .values(
            "id",
            "name",
            "description",
            "product__store_price",
            "product__retail_price",
        )
        .distinct()
    )

    media = models.Media.objects.filter(product__slug=slug)
    attributevalues = models.ProductAttributeValue.objects.all()
    product_category = models.Category.objects.get(product__slug=slug)
    product_attributes = (
        models.ProductTypeAttribute.objects.filter(
            product_type__product_type__product__slug=slug
        )
        .distinct()
        .values("product_attribute__name")
    )
    related_products = utils.relatedProducts(request, product_category)
    custom_range, related_products = utils.paginateProducts(
        request, related_products, 4
    )
    context = {
        "product_object": product,
        "media": media,
        "attribute_values": attributevalues,
        "related_products": related_products,
        "product_attributes": product_attributes,
    }
    return render(
        request,
        "products/single-product-view.html",
        context,
    )
