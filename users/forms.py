from django import forms
from users.models import Usuario

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class RegistrarUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = Usuario
        fields = ['nombre', 'identificacion', 'cargo', 'email', 'rol', 'password']