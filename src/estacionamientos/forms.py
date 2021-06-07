from django.forms import ModelForm
from django import forms
from .models import *

class AgregarHabitacionForms(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = [
            'user',
            'rut',
            'tipo_estacionamiento',
            'comuna_estacionamiento',
            'categoria_estacionamiento',
            'estado_estacionamiento',
            'calle',
            'numeracion',
        ]
        labels = {
            'user': 'Usuario',
            'rut': 'Rut',
            'tipo_estacionamiento': 'Tipo de estacionamiento',
            'comuna_estacionamiento': 'Comuna de estacionamiento',
            'categoria_estacionamiento': 'Categoría de estacionamiento',
            'estado_estacionamiento': 'Estado de estacionamiento',
            'calle': 'Calle',
            'numeracion': 'Numeración',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AV.Example'}),
            'numeracion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditarHabitacionForms(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = [
            'tipo_estacionamiento',
            'comuna_estacionamiento',
            'categoria_estacionamiento',
            'estado_estacionamiento',
            'calle',
            'numeracion',
        ]
        labels = {
            'tipo_estacionamiento': 'Tipo de estacionamiento',
            'comuna_estacionamiento': 'Comuna de estacionamiento',
            'categoria_estacionamiento': 'Categoría de estacionamiento',
            'estado_estacionamiento': 'Estado de estacionamiento',
            'calle': 'Calle',
            'numeracion': 'Numeración',
        }
        widgets = {
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AV.Example'}),
            'numeracion': forms.TextInput(attrs={'class': 'form-control'}),
        }