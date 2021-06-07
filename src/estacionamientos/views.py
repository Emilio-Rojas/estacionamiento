from django.shortcuts import render, redirect
from estacionamientos.forms import AgregarHabitacionForms, EditarHabitacionForms

from estacionamientos.models import Estacionamiento

#CRUD ESTACIONAMIENTO PARTICULAR

def estacionamiento_particular_listar(request):
    estacionamientos = Estacionamiento.objects.all().order_by('id')
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


    #CRUD ESTACIONAMIENTO PRIVADO

def disponibilidad_privado(request):
    estacionamientos = Estacionamiento.objects.all().order_by('id')
    return render(request, 'estacionamientos/disponibilidad_privado.html', {'estacionamientos': estacionamientos})
    
