from django.urls import path 
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('my-account/',views.updateProfile,name = 'my-account'),
    path('404/',views._404,name='404'),
]