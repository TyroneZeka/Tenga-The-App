from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from Products.admin import products_admin_site

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("admin/", products_admin_site.urls),  # tenga-admin
    path("users/", include("users.urls", namespace="users")),
    path("", include("Products.urls")),
    path("checkout/", include("Checkout.urls", namespace="checkout")),
    path("cart/", include("Cart.urls", namespace="cart")),
    path("orders/", include("Orders.urls", namespace="orders")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# admin.site.index_title = "Tenga Online Shopping System"
# admin.site.site_header = "Tenga Online Shopping System Admin"
# admin.site.site_title = "TOSS Admin"
