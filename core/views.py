from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from crud.models import *

# Create your views here.
@login_required
def root(request):
    return redirect('/home')

def home(request):
    return render(request,"core/home.html")

def productos(request):
    context =   { 'productos': Producto.objects.all()}
    return render(request,"core/productos.html",context)


def salir(request):
    logout(request)
    return redirect('/')

