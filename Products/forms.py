from django.forms import ModelForm

from . import models


class CartForm(ModelForm):
    class Meta:
        model = models.ProductMeta
        fields = []
