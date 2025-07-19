from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import es_admin, es_empleado
from django.contrib import messages
from .models import Servicio, Pago
from .forms import ServicioForm, PagoForm
from django.db.models import Sum
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods, require_GET

def es_admin_o_empleado(user):
    return user.is_authenticated and user.rol in ['ADMIN', 'EMPLEADO']

@csrf_protect
@require_GET
@login_required 
@user_passes_test(es_admin)
def admin_home(request):
    return render(request, 'service/admin_home.html')

@csrf_protect
@require_GET
@login_required
@user_passes_test(es_empleado) 
def empleado_home(request):
    return render(request, 'service/empleado_home.html')

@csrf_protect
@require_http_methods(["GET"])
@require_http_methods(["POST"])
@login_required
@user_passes_test(es_admin_o_empleado)
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.estado = 'Pendiente de Pago'
            servicio.save()
            messages.success(request, 'Servicio creado exitosamente.')
            return redirect('crear_servicio')
        else:
            messages.error(request, 'Error al crear el servicio. Revisa los datos.')
    else:
        form = ServicioForm()
    return render(request, 'service/crear_servicio.html', {'form': form})

@csrf_protect
@require_http_methods(["GET"])
@require_http_methods(["POST"])
@login_required
@user_passes_test(es_admin_o_empleado)
def pagar_servicio(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.usuario = request.user
            pago.save()
            messages.success(request, 'Pago registrado exitosamente.')
            return redirect('pagar_servicio')
        else:
            messages.error(request, 'Error al registrar el pago. Revisa los datos.')
    else:
        form = PagoForm()
    return render(request, 'service/pagar_servicio.html', {'form': form})

@require_GET
@login_required
def resumen_pagos(request):
    MESES = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    return render(request, 'service/resumen_pagos.html', {'meses': MESES})

@require_GET
@login_required
def resumen_pagos_por_mes(request, mes):
    pagos = Pago.objects.filter(mes=mes)
    total_mes = pagos.aggregate(total=Sum('valor'))['total'] or 0
    return render(request, 'service/resumen_detalle.html', {
        'pagos': pagos,
        'mes': mes,
        'total_mes': total_mes
    })
