from django import forms
from .models import Servicio, Pago

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['empresa', 'nombre_servicio', 'referencia_pago', 'quien_paga', 'centro_costo']

class PagoForm(forms.ModelForm):
    empresa = forms.ChoiceField(choices=Servicio.EMPRESAS, label='Empresa')

    class Meta:
        model = Pago
        fields = ['empresa', 'servicio', 'valor', 'mes', 'medio_pago']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicio'].queryset = Servicio.objects.filter(estado='Pendiente de Pago')