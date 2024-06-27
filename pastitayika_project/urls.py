"""
URL configuration for pastitayika_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from plantitayika_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('acerca-de/', views.pagina_acerca_de, name='pagina_acerca_de'),
    path('contacto/', views.pagina_contacto, name='pagina_contacto'),
    path('formulario/', views.pagina_formulario, name='pagina_formulario'),
    path('insumos/', views.pagina_insumos, name='pagina_insumos'),
    path('maceteros/', views.pagina_maceteros, name='pagina_maceteros'),
    path('productos/', views.pagina_productos, name='pagina_productos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
