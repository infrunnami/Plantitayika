# plantitayika_app/views.py
from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'plantitayika_app/PaginaInicio.html')

def pagina_acerca_de(request):
    return render(request, 'plantitayika_app/PaginaAcercaDe.html')

def pagina_contacto(request):
    return render(request, 'plantitayika_app/PaginaContacto.html')

def pagina_formulario(request):
    return render(request, 'plantitayika_app/PaginaFormulario.html')

def pagina_insumos(request):
    return render(request, 'plantitayika_app/PaginaInsumos.html')

def pagina_maceteros(request):
    return render(request, 'plantitayika_app/PaginaMaceteros.html')

def pagina_productos(request):
    return render(request, 'plantitayika_app/PaginaProductos.html')
