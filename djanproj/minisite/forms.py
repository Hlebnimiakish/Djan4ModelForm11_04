# from django import forms
from django.forms import ModelForm
from .models import Customer

# class CustomerForm(forms.Form):
#     firstname = forms.CharField(max_length=255)
#     lastname = forms.CharField(max_length=255)

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname']