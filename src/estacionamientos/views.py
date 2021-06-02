from django.shortcuts import render, redirect

def administrar_estacionamiento(request):
    return render(request, 'estacionamientos/administrar_estacionamiento.html', {})


def estacionamiento_privado(request):
    return render(request, 'estacionamientos/estacionamiento_privado.html', {})
