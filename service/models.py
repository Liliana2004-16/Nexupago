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
    EMPRESAS = [
        ('Enel', 'Enel'),
        ('Vanti', 'Vanti'),
        ('Acueducto_Emservilla', 'Acueducto Emservilla'),
        ('Acueducto_Bogota', 'Acueducto Bogotá'),
        ('ETB', 'ETB'),
        ('Admon', 'Admon'),
    ]

    CENTROS_COSTO = [
        ('Centro1', 'Centro de Costo 1'),
        ('Centro2', 'Centro de Costo 2'),
        ('Centro3', 'Centro de Costo 3'),
        ('Centro14', 'Centro de Costo 14'),
        ('Centro15', 'Centro de Costo 15'),
        ('Centro16', 'Centro de Costo 16'),
        ('Centro999', 'Centro de Costo 999')
    ]

    empresa = models.CharField(max_length=100, choices=EMPRESAS)
    nombre_servicio = models.CharField(max_length=100)
    referencia_pago = models.CharField(max_length=100)
    centro_costo = models.CharField(max_length=100, choices=CENTROS_COSTO, default='Centro1')
    estado = models.CharField(default='Pendiente de Pago', max_length=50)

    def __str__(self):
        return f"{self.nombre_servicio} - {self.empresa}"

class Pago(models.Model):
    MESES = [
        ('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'),
        ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'),
        ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre'),
    ]

    MEDIOS_PAGO = [
        ('Transferencia', 'Transferencia'),
        ('Efectivo', 'Efectivo'),
        ('PSE', 'PSE'),
        ('Tarjeta', 'Tarjeta'),
    ]

    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    mes = models.CharField(max_length=15, choices=MESES)
    medio_pago = models.CharField(max_length=20, choices=MEDIOS_PAGO)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.servicio} - {self.mes} - {self.valor}"
