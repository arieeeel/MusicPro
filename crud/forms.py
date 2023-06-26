from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'descripcion',
            'precio',
            'stock',
            'imagen',
            'marca'
        ]
        labels = {
            'idProducto': 'Código Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio Unitario',
            'stock': 'Stock',
            'imagen': 'Imagen',
            'marca': 'Marca'
        }
        widgets = {
            'idProducto': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'}),
            'marca': forms.Select(attrs={'class':'form-control'})
        }