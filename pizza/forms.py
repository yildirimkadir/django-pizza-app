from socket import fromshare
from django import forms
from .models import Pizza, Size

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__' 
        # labels = {"first_name": "Name"}

class MultiplePizzaForm(forms.Form):
 number = forms.IntegerField(min_value=2, max_value=6)