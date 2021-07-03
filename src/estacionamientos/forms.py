from django.forms import ModelForm
from django import forms
from .models import *

class AgregarEstacionamientoForms(forms.ModelForm):
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
            'precio_base',
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
            'precio_base': 'Precio Base',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese rut'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AV.Example'}),
            'numeracion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234'}),
            'precio_base': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }

class EditarEstacionamientoForms(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = [
            'user',
            'tipo_estacionamiento',
            'comuna_estacionamiento',
            'categoria_estacionamiento',
            'estado_estacionamiento',
            'calle',
            'numeracion',
            'precio_base',
        ]
        labels = {
            'user': 'Usuario',
            'tipo_estacionamiento': 'Tipo de estacionamiento',
            'comuna_estacionamiento': 'Comuna de estacionamiento',
            'categoria_estacionamiento': 'Categoría de estacionamiento',
            'estado_estacionamiento': 'Estado de estacionamiento',
            'calle': 'Calle',
            'numeracion': 'Numeración',
            'precio_base': 'Precio Base',
        }
        widgets = {
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AV.Example'}),
            'numeracion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_base': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }

class AgregarDisponibilidadForms(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = [
            'estacionamiento',
            'fecha_disponibilidad',
            'precio_bloque',
        ]
        labels = {
            'estacionamiento': 'Disponibilidad',
            'fecha_disponibilidad': 'Fecha Disponibilidad',
            'precio_bloque': 'Precio por bloque',

        }
        widgets = {
            'fecha_disponibilidad': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'precio_bloque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }

class EditarDisponibilidadForms(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = [
            'fecha_disponibilidad',
            'precio_bloque'
        ]
        labels = {
            'fecha_disponibilidad': 'Fecha Disponibilidad',
            'precio_bloque': 'Precio por bloque',
        }
        widgets = {
            'fecha_disponibilidad': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'precio_bloque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }

class AgregarBloqueDisponibilidadForms(forms.ModelForm):
    class Meta:
        model = BloqueDisponibilidad
        fields = [
            'disponibilidad',
            'bloque_inicio',
            'bloque_termino',
        ]
        labels = {
            'disponibilidad': 'Disponibilidad',
            'bloque_inicio': 'Bloque Inicio',
            'bloque_termino': 'Bloque Termino',
        }

class EditarBloqueDisponibilidadForms(forms.ModelForm):
    class Meta:
        model = BloqueDisponibilidad
        fields = [
            'bloque_inicio',
            'bloque_termino',
        ]
        labels = {
            'bloque_inicio': 'Bloque Inicio',
            'bloque_termino': 'Bloque Termino',
        }