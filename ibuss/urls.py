"""ibuss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('maestros.paises.urls')), #new
    path('paises/<int:pk>',include('maestros.paises.urls')), #new
    path('',include('maestros.estados.urls')), #new
    path('estados/<int:pk>',include('maestros.estados.urls')), #new
    path('',include('maestros.municipios.urls')), #new
    path('municipios/<int:pk>',include('maestros.municipios.urls')), #new
    path('',include('maestros.parroquias.urls')), #new
    path('parroquias/<int:pk>',include('maestros.parroquias.urls')), #new
    path('',include('maestros.ciudades.urls')), #new
    path('ciudades/<int:pk>',include('maestros.ciudades.urls')), #new
    path('',include('maestros.aplicaciones.urls')), #new
    path('aplicaciones/<int:pk>',include('maestros.aplicaciones.urls')), #new
    path('',include('maestros.miscelaneos.urls')), #new
    path('miscelaneos/<int:pk>',include('maestros.miscelaneos.urls')), #new
    path('',include('maestros.miscelaneosdet.urls')), #new
    path('miscelaneosdet/<int:pk>',include('maestros.miscelaneosdet.urls')), #new
    path('',include('maestros.bancos.urls')), #new
    path('bancos/<int:pk>',include('maestros.bancos.urls')), #new
    path('',include('maestros.personas.urls')), #new
    path('personas/<int:pk>',include('maestros.personas.urls')), #new
    path('',include('maestros.monedas.urls')), #new
    path('monedas/<int:pk>',include('maestros.monedas.urls')), #new
    path('',include('maestros.parametros.urls')), #new
    path('parametros/<int:pk>',include('maestros.parametros.urls')), #new
    path('',include('maestros.companias.urls')), #new
    path('companias/<int:pk>',include('maestros.companias.urls')), #new
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


