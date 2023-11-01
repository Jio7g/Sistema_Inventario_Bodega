from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class RegistroSalidaForm(forms.Form):
    codigo = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
