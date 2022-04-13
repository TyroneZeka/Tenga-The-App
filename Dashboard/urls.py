from django.urls import include, path,re_path
from . import views


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('settings/',views.settings,name='settings'),  
    path('tables/',views.tables,name='tables'),
]
