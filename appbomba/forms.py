from django import forms
from .models import CarroBomba

class CarroForm(forms.ModelForm):
    class Meta:
        model= CarroBomba
        fields = '__all__'