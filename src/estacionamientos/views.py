from django.shortcuts import render, redirect

def administrar_estacionamientos(request):
    return render(request, 'estacionamientos/administrar_estacionamiento.html', {})
