from django import forms
from drivers.models import Driver

class CarForm(forms.Form):
    brand = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'user-input'}))
    model = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'user-input'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'user-input'}))
    vin = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'user-input'}))
    owner = forms.ModelChoiceField(queryset=Driver.objects.all() )