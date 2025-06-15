from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('crear/', views.crear_servicio, name='crear_servicio'),
    path('pagar/', views.pagar_servicio, name='pagar_servicio'),
    path('resumen/', views.resumen_pagos, name='resumen_pagos'),
]
