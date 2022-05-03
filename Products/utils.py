from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from . import models


def searchProduct(request, order):
    search_query = ""

    if request.GET.get("query"):
        search_query = request.GET.get("query")

    categories = models.Category.objects.filter(name__icontains=search_query)

    # x = models.Product.objects.get(category__name="woman")
    # print(x)

    products = (
        models.Product.objects.distinct()
        .filter(
            Q(name__icontains=search_query)
            | Q(slug__icontains=search_query)
            | Q(category__name__iexact=search_query)
        )
        .order_by(order)
    )
    return products, search_query


def relatedProducts(request, category):
    products = models.Product.objects.distinct().filter(
        category__name=category
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

    leftIndex = int(page) - 2

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 10
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return (custom_range, products)
