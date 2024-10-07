from django import forms
from .models import *

class AddProductForm(forms.ModelForm):
    product_name = forms.TextInput()
    description = forms.TextInput()
    price = forms.DecimalField()
    expiration_date = forms.DateField()
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'expiration_date']
