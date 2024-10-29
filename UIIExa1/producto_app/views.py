from django.shortcuts import render
from .models import products

# Create your views here.

def index_vista(request):
    ListaProductos=products.objects.all()
    return render(request,'gestionarProd.html',{"productos":ListaProductos})