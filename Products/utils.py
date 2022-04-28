from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from . import models


def searchProduct(request):
    search_query = ""

    if request.GET.get("query"):
        search_query = request.GET.get("query")

    products = (
        models.Product.objects.distinct()
        .filter(
            Q(name__icontains=search_query) | Q(slug__icontains=search_query)
        )
        .values(
            "name",
            "slug",
            "description",
            "product__store_price",
            "product__retail_price",
            "product__id",
        )
        .order_by("-product__id")
    )
    return products


def paginateProducts(request, products, results):
    page = request.GET.get("page")
    paginator = Paginator(products, results)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    leftIndex = int(page) - 4

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 5
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return (custom_range, products)
