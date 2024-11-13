from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

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

    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')  

def index(request):
    return render(request, 'index.html')
