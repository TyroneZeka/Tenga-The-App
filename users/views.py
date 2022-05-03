from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from Orders.models import Order
from Orders.views import user_orders

from .forms import CustomUserCreationForm, UserAddressForm, UserEditForm
from .models import Address, Customer
from .token import account_activation_token


# Create your views here.
def signup(request):
    page = "signup"
    if request.user.is_authenticated:
        return redirect("/")
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.set_password(form.cleaned_data["password1"])
            user.username = user.username.lower()
            user.is_active = True
            user.save()
            # Set up for account activation Email
            current_site = get_current_site(request)
            subject = "Activate your Account"
            message = render_to_string(
                "users/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.id)),
                    "token": account_activation_token.make_token(user),
                },
            )
            # user.email_user(subject=subject, message=message)
            messages.success(request, "User Account Created!")
            return redirect("users:login")

            # login(request, user)
            # return redirect("/")

    return render(request, "users/signup.html", {"form": form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("/")
    else:
        return render(request, "users/activation_invalid.html")


def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect(request.GET["next"] if "next" in request.GET else "/")

    if request.method == "POST":
        # TODO: implement for both username and email for login
        username = request.POST["username"]
        password = request.POST["password"]
        username = username.lower()

        try:
            user = Customer.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist!")

        # authenticate is checking the users account not the customer account
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(
                request.POST.get("next") if "next" in request.POST else "/"
            )
        else:
            messages.error(request, "Username OR password is incorrect")

    return render(request, "users/login.html", {})


@login_required(login_url="users:login")
def logoutUser(request):
    logout(request)
    return redirect("/")


@login_required(login_url="users:login")
def dashboard(request):
    orders = user_orders(request)
    return render(
        request,
        "users/dashboard.html",
        {"section": "profile", "orders": orders},
    )


@login_required(login_url="users:login")
def edit_details(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == "POST":
        user_form = UserEditForm(
            request.POST, request.FILES, instance=customer
        )
        if user_form.is_valid():
            customer = 1
            user_form.save()

    else:
        user_form = UserEditForm(instance=customer)

    return render(
        request,
        "users/edit_details.html",
        {"user_form": user_form},
    )


@login_required(login_url="users:login")
def delete_user(request):
    user = Customer.objects.get(username=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect("users:delete_confirmation")


@login_required(login_url="users:login")
def view_address(request):
    customer = Customer.objects.get(user=request.user)
    addresses = Address.objects.filter(customer_id=customer.id)
    return render(request, "users/addresses.html", {"addresses": addresses})


@login_required(login_url="users:login")
def add_address(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address = address_form.save(commit=False)
            address.customer_id = customer
            address.save()
            return HttpResponseRedirect(reverse("users:addresses"))
    else:
        address_form = UserAddressForm()
    return render(
        request,
        "users/edit_addresses.html",
        {"form": address_form},
    )


@login_required(login_url="users:login")
def edit_address(request, id):
    customer = Customer.objects.get(user=request.user)
    if request.method == "POST":
        address = Address.objects.get(pk=id, customer_id=customer.id)
        address_form = UserAddressForm(instance=address, data=request.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse("users:addresses"))
    else:
        address = Address.objects.get(pk=id, customer_id=customer.id)
        address_form = UserAddressForm(instance=address)
    return render(
        request,
        "users/edit_addresses.html",
        {"form": address_form},
    )


@login_required(login_url="users:login")
def delete_address(request, id):
    address = Address.objects.filter(pk=id, customer=request.user).delete()
    return redirect("users:addresses")


@login_required(login_url="users:login")
def set_default(request, id):
    customer = Customer.objects.get(user=request.user)
    Address.objects.filter(customer_id=customer, default=True).update(
        default=False
    )
    Address.objects.filter(pk=id, customer_id=customer).update(default=True)

    previous_url = request.META.get("HTTP_REFERER")

    if "delivery_address" in previous_url:
        return redirect("checkout:delivery_address")

    return redirect(previous_url)


@login_required(login_url="users:login")
def user_orders(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(user=customer).filter(billing_status=True)

    return render(request, "users/user_orders.html", {"orders": orders})
