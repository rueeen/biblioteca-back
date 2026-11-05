from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import PerfilForm
from .models import Perfil

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('list-book')

    if request.method == "POST":
        # iniciando sesion
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()      
            perfil, _ = Perfil.objects.get_or_create(usuario=user)
            login(request, user)
            return redirect('list-book')
    else:
        form = AuthenticationForm()
            
    return render(request, 'registro/login.html', {'form':form})

def registrar_view(request):
    form = PerfilForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado")
            return redirect('login')
    return render(request, 'registro/registrar.html', {'form':form})

def error403View(request):
    return render(request, 'registro/error_login.html')

def logoutView(request):    
    logout(request)
    return redirect('login')