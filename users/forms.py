from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm, UserCreationForm)
from django.contrib.auth.models import User

from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs = {
            "placeholder": "First Name",
            "class": "form-control mb-3",
            "id": "form-firstname",
        }
        self.fields["last_name"].widget.attrs = {
            "placeholder": "Last Name",
            "class": "form-control mb-3",
            "id": "form-lastname",
        }
        self.fields["email"].widget.attrs = {
            "placeholder": "Email",
            "class": "form-control mb-3",
            "id": "form-email",
        }
        self.fields["username"].widget.attrs = {
            "placeholder": "Username",
            "class": "form-control mb-3",
            "id": "form-username",
        }
        self.fields["password1"].widget.attrs = {
            "placeholder": "Password",
            "class": "form-control mb-3",
            "id": "form-password1",
        }
        self.fields["password2"].widget.attrs = {
            "placeholder": "Confirm Password",
            "class": "form-control mb-3",
            "id": "form-password2",
        }


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label="Account email (can not be changed)",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "email",
                "id": "form-email",
                "readonly": "readonly",
            }
        ),
    )
    username = forms.CharField(
        label="Username (can not be changed)",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "username",
                "id": "form-email",
                "readonly": "readonly",
            }
        ),
    )

    class Meta:
        model = models.Customer
        fields = (
            "email",
            "username",
            "firstName",
            "lastName",
            "phone",
            "profilePicture",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        self.fields["username"].required = True
        self.fields["firstName"].widget.attrs = {
            "placeholder": "First Name",
            "class": "form-control mb-3",
            "id": "form-firstname",
        }
        self.fields["lastName"].widget.attrs = {
            "placeholder": "Last Name",
            "class": "form-control mb-3",
            "id": "form-lastname",
        }
        self.fields["phone"].widget.attrs = {
            "class": "form-control mb-3",
            "placeholder": "Phone Number",
            "id": "form-phone",
        }


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = [
            "address1",
            "address2",
            "city",
            "post_code",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["address1"].widget.attrs.update(
            {
                "class": "form-control mb-2 address_form",
                "placeholder": "Address Line 1",
            }
        )
        self.fields["address2"].widget.attrs.update(
            {
                "class": "form-control mb-2 address_form",
                "placeholder": "Address Line 2",
            }
        )
        self.fields["city"].widget.attrs.update(
            {
                "class": "form-control mb-2 address_form",
                "placeholder": "City",
            }
        )
        self.fields["post_code"].widget.attrs.update(
            {
                "class": "form-control mb-2 address_form",
                "placeholder": "Post Code",
            }
        )
