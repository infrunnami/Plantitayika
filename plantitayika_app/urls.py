from django.urls import path
from . import views

urlpatterns = [
    path('acerca_de/', views.PaginaAcercaDe, name='PaginaAcercaDe'),
    path('contacto/', views.PaginaContacto, name='PaginaContacto'),
    path('formulario/', views.PaginaFormulario, name='PaginaFormulario'),
    path('insumos/', views.PaginaInsumos, name='PaginaInsumos'),
    path('maceteros/', views.PaginaMaceteros, name='PaginaMaceteros'),
    path('productos/', views.PaginaProductos, name='PaginaProductos'),
]