from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "users"

urlpatterns = [
    path("register-new-user/", views.signup, name="signup"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("activate/<slug:uidb64>/<slug:token>)/",views.account_activate,name="activate",),
    # User Profile Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/edit/", views.edit_details, name="edit_details"),
    path("profile/delete_user/", views.delete_user, name="delete_user"),
    path("profile/delete_confirm/",TemplateView.as_view(template_name="users/delete_confirm.html"),name="delete_confirmation",),
    path("addresses/", views.view_address, name="addresses"),
    path("add_address/", views.add_address, name="add_address"),
    path("addresses/edit/<slug:id>/", views.edit_address, name="edit_address"),
    path("addresses/delete/<slug:id>/",views.delete_address,name="delete_address",),
    path("addresses/set_default/<slug:id>/",views.set_default,name="set_default",),
    path("user_orders/", views.user_orders, name="user_orders"),
]
