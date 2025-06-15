from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'services/home.html')
@login_required
def crear_servicio(request):
    # lógica aquí
    return render(request, 'service/crear_servicio.html')
@login_required
def pagar_servicio(request):
    # lógica aquí
    return render(request, 'service/pagar_servicio.html')
@login_required
def resumen_pagos(request):
    # lógica aquí
    return render(request, 'service/resumen_pagos.html')