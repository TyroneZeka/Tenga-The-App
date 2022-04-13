"""Base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from Products.admin import products_admin_site

urlpatterns = [
    # path('admin/', products_admin_site.urls),
    path('shopadmin/',products_admin_site.urls), #tenga-admin
    path('users/',include('users.urls')),
    path('',include('Products.urls')),
    path('shop-admin/',include('Dashboard.urls'))
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


# admin.site.index_title = "Tenga Online Shopping System"
# admin.site.site_header = "Tenga Online Shopping System Admin"
# admin.site.site_title = "TOSS Admin"