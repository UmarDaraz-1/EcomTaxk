from django import forms
from .models import *

class SearchForm(forms.Form):
    name = forms.CharField(label='Product Name', max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), required=False)
    price_min = forms.DecimalField(label='Min Price', max_digits=10, decimal_places=2, required=False)
    price_max = forms.DecimalField(label='Max Price', max_digits=10, decimal_places=2, required=False)
