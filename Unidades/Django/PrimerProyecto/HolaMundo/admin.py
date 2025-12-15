from django.contrib import admin

# Register your models here.
#Añadimos esta linea para comenzar con el registro.
from HolaMundo.models import Author
#Forma de registrar la tabla Author
admin.site.register(Author)