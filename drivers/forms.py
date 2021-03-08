from django.forms import ModelForm
from .models import Driver

class DriverForm(ModelForm):
    # name = forms.CharField(label='Name:', max_length=255, widget=forms.TextInput(attrs={'class': 'user-input'}))
    # license = forms.CharField(label='License:', max_length=64, widget=forms.TextInput(attrs={'class': 'user-input'}))
    class Meta:
        model = Driver
        fields = ['name', 'license']