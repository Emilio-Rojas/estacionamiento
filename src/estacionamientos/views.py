from django.shortcuts import render, redirect

def administrar_estacionamientos(request):
    return render(request, 'estacionamientos/administrar_estacionamiento.html', {})

def administrar_estacionamientos_particular(request):
    return render(request, 'estacionamientos/administrar_estacionamiento_particular.html', {})