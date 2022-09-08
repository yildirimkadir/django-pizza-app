from socket import fromshare
from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__' 
        # labels = {"first_name": "Name"}