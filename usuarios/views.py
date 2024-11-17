from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guardamos aún para asignar la contraseña
            user.set_password(form.cleaned_data['password'])  # Encriptamos la contraseña con el método set_password, clean_data para obtener los datos limpios del formulario
            user.save()#Guardamos el usuario
            # Asignamos el rol al perfil
            user.perfil.rol = form.cleaned_data['rol']
            user.perfil.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('usuarios:login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Obtener el usuario autenticado
            login(request, user)
            return redirect('usuarios:index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')  # Mensaje cuando no es válido
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')  

@login_required
def index(request):
    return render(request, 'index.html')
