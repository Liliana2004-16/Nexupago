from django.contrib import admin
from .models import Empresa, Servicio, Pago, CentroCosto
admin.site.register(Empresa)
admin.site.register(Servicio)
admin.site.register(Pago)
admin.site.register(CentroCosto)