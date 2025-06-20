from django import forms
from .models import Servicio, Pago

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['empresa', 'nombre_servicio', 'referencia_pago', 'centro_costo']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['servicio', 'valor', 'mes', 'medio_pago']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Solo servicios pendientes
        self.fields['servicio'].queryset = Servicio.objects.filter(
            estado='Pendiente de Pago'
        )