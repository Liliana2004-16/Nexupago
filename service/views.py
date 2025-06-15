from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import es_admin, es_empleado
from django.contrib import messages
from .models import Servicio
from .forms import ServicioForm, PagoForm
from users.decorators import rol_required

@login_required
def admin_home(request):
    return render(request, 'service/admin_home.html')

@login_required
def empleado_home(request):
    return render(request, 'service/empleado_home.html')

@login_required
def crear_servicio(request):
     if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.estado = 'Pendiente de pago'
            servicio.save()
            messages.success(request, 'Servicio creado exitosamente.')
            return redirect('crear_servicio')  # o la ruta que desees
        else:
            print("Formulario inválido", form.errors) 
     else:
        form = ServicioForm()
     return render(request, 'service/crear_servicio.html', {'form': form})

@login_required
def pagar_servicio(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagar_servicio')  # o donde necesites
    else:
        form = PagoForm()

    return render(request, 'services/pagar_servicio.html', {'form': form}) 
    
@login_required
def resumen_pagos(request):
    # lógica aquí
    return render(request, 'service/resumen_pagos.html')


#restrcciones
def es_admin_o_empleado(user):
    return user.is_authenticated and user.rol in ['ADMIN', 'EMPLEADO']

@login_required
@user_passes_test(es_admin_o_empleado)
def crear_servicio(request):
    return render(request, 'service/crear_servicio.html')

@login_required
@user_passes_test(es_admin_o_empleado)
def pagar_servicio(request):
    return render(request, 'service/pagar_servicio.html')

@login_required
@user_passes_test(es_admin_o_empleado)
def mostrar_lista(request):
    return render(request, 'service/mostrar_lista.html')