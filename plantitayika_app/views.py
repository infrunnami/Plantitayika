# plantitayika_app/views.py
from django.shortcuts import render
from .models import Plantas, Insumos, Maceteros, Clientes

def pagina_inicio(request):
    return render(request, 'plantitayika_app/PaginaInicio.html')

def pagina_acerca_de(request):
    return render(request, 'plantitayika_app/PaginaAcercaDe.html')

def pagina_contacto(request):
    return render(request, 'plantitayika_app/PaginaContacto.html')

def pagina_formulario(request):
    vClientes= Clientes.objects.all()
    context={"vInsumos":vClientes}
    return render(request, 'plantitayika_app/PaginaFormulario.html')

""" def registrarCliente(request):
    nombre = request.POST["name"]
    email = request.POST["name"]
    contrasena = request.POST["name"]
    numero = request.POST["name"]
 """


def pagina_insumos(request):
    vInsumos= Insumos.objects.all()
    context={"vInsumos":vInsumos}
    return render(request, 'plantitayika_app/PaginaInsumos.html',context)

def pagina_maceteros(request):
    vMaceteros= Maceteros.objects.all()
    context={"vInsumos":vMaceteros}
    return render(request, 'plantitayika_app/PaginaMaceteros.html',context)

def pagina_productos(request):
    return render(request, 'plantitayika_app/PaginaProductos.html')

def index(request):
    return render(request, 'Alumnos/index.html', context)