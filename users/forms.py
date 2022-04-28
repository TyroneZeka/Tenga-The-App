from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

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
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs[
            "placeholder"
        ] = "Confirm PAssword"

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = [
            "firstName",
            "lastName",
            "email",
            "username",
            "profilePicture",
            "bio",
            "phone",
        ]

        def __init__(self, *args, **kwargs):
            super(CustomerForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({"class": "input"})
