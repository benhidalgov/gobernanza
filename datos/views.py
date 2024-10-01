from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# datos/views.py

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

# Vista para la página principal

# Vista para la página principal


from django.shortcuts import render

# Vista para la página principal


def index(request):
    return render(request, 'index.html')


# Vista para la página de actualización


def actualizacion(request):
    return render(request, 'actualizacion.html')

# Vista para la página de login


def login_view(request):
    return render(request, 'login.html')
