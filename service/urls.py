from django.urls import path
from . import views


urlpatterns = [
    path('admin/inicio/', views.admin_home, name='admin_home'),
    path('empleado/inicio/', views.empleado_home, name='empleado_home'),
    path('crear/', views.crear_servicio, name='crear_servicio'),
    path('pagar/', views.pagar_servicio, name='pagar_servicio'),
    path('resumen/', views.resumen_pagos, name='resumen_pagos'),
     path('resumen_pagos/<str:mes>/', views.resumen_pagos_por_mes, name='resumen_pagos_mes'),
]
