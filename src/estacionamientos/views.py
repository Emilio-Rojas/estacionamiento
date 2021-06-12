from django.shortcuts import render, redirect
from estacionamientos.forms import AgregarDisponibilidadForms, AgregarHabitacionForms, EditarDisponibilidadForms, EditarHabitacionForms

from estacionamientos.models import Disponibilidad, Estacionamiento

def disponibilidad_estacionamiento(request):
    return render(request, 'estacionamientos/disponibilidad_estacionamiento.html', {})

#CRUD ESTACIONAMIENTO PARTICULAR

def estacionamiento_particular_listar(request):
    estacionamientos = Estacionamiento.objects.filter(tipo_estacionamiento=1).order_by('id')
    return render(request, 'estacionamientos/estacionamiento_particular_listar.html', {'estacionamientos': estacionamientos})

def estacionamiento_particular_agregar(request):
    if request.method == 'POST':
        form = AgregarHabitacionForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/estacionamiento/particular/listar')
    else:
        form = AgregarHabitacionForms()
    return render(request, 'estacionamientos/estacionamiento_particular_agregar.html',{'form' : form})

def estacionamiento_particular_editar(request, id_estacionamiento):
    estacionamiento = Estacionamiento.objects.get(id=id_estacionamiento)
    if request.method == "GET":
        form = EditarHabitacionForms(instance=estacionamiento)
    else:
        form = EditarHabitacionForms(request.POST, request.FILES,instance=estacionamiento)
        if form.is_valid():
            estacionamiento = form.save(commit=False)
            estacionamiento.save()
        return redirect('/estacionamiento/particular/listar')
    return render(request, "estacionamientos/estacionamiento_particular_editar.html", {'form': form})

def estacionamiento_particular_eliminar(request, id_estacionamiento):
    estacionamiento = Estacionamiento.objects.get(id=id_estacionamiento)
    if request.method == 'POST':
        estacionamiento.delete()
        return redirect('/estacionamiento/particular/listar')
    return render(request, 'estacionamientos/estacionamiento_particular_eliminar.html', {'estacionamiento': estacionamiento})

#CRUD DISPONIBILIDAD

def estacionamiento_disponibilidad_detalle(request, id_estacionamiento):
    estacionamiento = Estacionamiento.objects.get(id=id_estacionamiento)
    disponibilidades = Disponibilidad.objects.filter(estacionamiento=id_estacionamiento)
    return render(request, 'estacionamientos/estacionamiento_disponibilidad_detalles.html', {'estacionamiento': estacionamiento, 'disponibilidades': disponibilidades})

def estacionamiento_disponibilidad_agregar(request, id_estacionamiento):
    id_estacionamiento = id_estacionamiento
    if request.method == 'POST':
        form = AgregarDisponibilidadForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/estacionamiento/detalle/' + str(id_estacionamiento))
    else:
        form = AgregarDisponibilidadForms()
    return render(request, 'estacionamientos/estacionamiento_disponibilidad_agregar.html',{'form' : form, 'id_estacionamiento':id_estacionamiento})

def estacionamiento_disponibilidad_editar(request, id_estacionamiento, id_disponibilidad):
    id_estacionamiento = id_estacionamiento
    disponibilidad = Disponibilidad.objects.get(id=id_disponibilidad)
    if request.method == "GET":
        form = EditarDisponibilidadForms(instance=disponibilidad)
    else:
        form = EditarDisponibilidadForms(request.POST, request.FILES,instance=disponibilidad)
        if form.is_valid():
            estacionamiento = form.save(commit=False)
            estacionamiento.save()
        return redirect('/estacionamiento/disponibilidad/' + str(id_estacionamiento))
    return render(request, "estacionamientos/estacionamiento_disponibilidad_editar.html", {'form': form, 'id_estacionamiento': id_estacionamiento})

def estacionamiento_disponibilidad_eliminar(request, id_estacionamiento, id_disponibilidad):
    id_estacionamiento = id_estacionamiento
    disponibilidad = Disponibilidad.objects.get(id=id_disponibilidad)
    if request.method == 'POST':
        disponibilidad.delete()
        return redirect('/estacionamiento/disponibilidad/' + str(id_estacionamiento))
    return render(request, 'estacionamientos/estacionamiento_disponibilidad_eliminar.html', {'id_estacionamiento': id_estacionamiento})

#CRUD ESTACIONAMIENTO PRIVADO

def estacionamiento_privado_listar(request):
    estacionamientos = Estacionamiento.objects.filter(tipo_estacionamiento=2).order_by('id')
    return render(request, 'estacionamientos/estacionamiento_privado_listar.html', {'estacionamientos': estacionamientos})

def estacionamiento_privado_agregar(request):
    if request.method == 'POST':
        form = AgregarHabitacionForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/estacionamiento/privado/listar')
    else:
        form = AgregarHabitacionForms()
    return render(request, 'estacionamientos/estacionamiento_privado_agregar.html',{'form' : form})

def estacionamiento_privado_editar(request, id_estacionamiento):
    estacionamiento = Estacionamiento.objects.get(id=id_estacionamiento)
    if request.method == "GET":
        form = EditarHabitacionForms(instance=estacionamiento)
    else:
        form = EditarHabitacionForms(request.POST, request.FILES,instance=estacionamiento)
        if form.is_valid():
            estacionamiento = form.save(commit=False)
            estacionamiento.save()
        return redirect('/estacionamiento/privado/listar')
    return render(request, "estacionamientos/estacionamiento_privado_editar.html", {'form': form})

def estacionamiento_privado_eliminar(request, id_estacionamiento):
    estacionamiento = Estacionamiento.objects.get(id=id_estacionamiento)
    if request.method == 'POST':
        estacionamiento.delete()
        return redirect('/estacionamiento/privado/listar')
    return render(request, 'estacionamientos/stacionamiento_privado_eliminar.html', {'estacionamiento': estacionamiento})
