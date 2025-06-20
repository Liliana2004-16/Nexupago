from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import LoginForm, RegistrarUsuarioForm
from django.contrib import messages
from users.utils import es_admin

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                if user.rol == 'ADMIN':
                    return redirect('admin_home')
                else:
                    return redirect('empleado_home')
            else:
                messages.error(request, "Correo o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')  

@user_passes_test(es_admin)
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])  # Encriptar contraseña
            usuario.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('registrar_usuario')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'users/registrar_usuario.html', {'form': form})

def home(request):
    # contenido o lógica pendiente de definir
    pass

def logout_usuario(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(es_admin)
def gestion_usuarios(request):
    return render(request, 'users/registrar_usuario.html')