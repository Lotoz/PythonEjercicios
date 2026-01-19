"""
URL configuration for PrimerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

from HolaMundo import views # Importo nuestro módulo views AQUI SE EXPORTAN TOdOS LOS METODOS
urlpatterns = [
    path('', views.home), #indicamos que la vista la queremos mostrar en esa   ruta.
#Si ponemos path('', views.index), no haría falta poner en el navegador el directorio.
    path('home/', views.home), #nueva vista
    path('admin/', admin.site.urls),
 
    path('autor/',views.autor_list),
    path('libro/',views.libro_list),
    path ('new-autor/',views.autor_create)
]