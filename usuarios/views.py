
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'login/login.html')



@login_required
def inventario(request):
    return render(request, 'index.html')
