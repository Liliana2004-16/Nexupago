from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroUsuarioForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def es_admin(user):
    return user.is_authenticated and user.rol == 'Administrador'

@login_required
@user_passes_test(es_admin)
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/registrar_usuario.html', {'form': RegistroUsuarioForm(), 'mensaje': 'Usuario registrado con éxito'})
    else:
        form = RegistroUsuarioForm()
    return render(request, 'users/registrar_usuario.html', {'form': form})
# inicio de sesion 
def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            print(f"[DEBUG] Usuario autenticado: {usuario.username}, Rol: {usuario.rol}")  # <-- agrega esto temporalmente
            return redirect('home')
        else:
            messages.error(request, "Correo o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_usuario(request):
    logout(request)
    return redirect('login')
