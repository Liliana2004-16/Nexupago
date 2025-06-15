from django.db import models
from users.models import Usuario

MEDIOS_PAGO = (
    ('Transferencia', 'Transferencia'),
    ('Efectivo', 'Efectivo'),
    ('Cheque', 'Cheque'),
    ('Otro', 'Otro'),
)

class Empresa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class CentroCosto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    )

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre_servicio = models.CharField(max_length=100)
    referencia_pago = models.CharField(max_length=100)
    quien_paga = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"{self.nombre_servicio} - {self.empresa}"

class Pago(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    mes = models.CharField(max_length=20)
    medio_pago = models.CharField(max_length=20, choices=MEDIOS_PAGO)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.servicio.nombre_servicio} - {self.mes}"
