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
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese rut'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AV.Example'}),
            'numeracion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234'}),
        }

class EditarEstacionamientoForms(forms.ModelForm):
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

class AgregarDisponibilidadForms(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = [
            'estacionamiento',
            'fecha_disponibilidad',
        ]
        labels = {
            'estacionamiento': 'Disponibilidad',
            'fecha_disponibilidad': 'Fecha Disponibilidad',
        }
        widgets = {
            'fecha_disponibilidad': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }

class EditarDisponibilidadForms(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = [
            'fecha_disponibilidad',
        ]
        labels = {
            'fecha_disponibilidad': 'Fecha Disponibilidad',
        }
        widgets = {
            'fecha_disponibilidad': forms.SelectDateWidget(attrs={'class': 'form-control'}),
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