from django.contrib import admin

# Register your models here.
#Añadimos esta linea para comenzar con el registro.
from HolaMundo.models import Author
from HolaMundo.models import Book
#Forma de registrar la tabla Author
admin.site.register(Author)
#Registrar tabla libro
admin.site.register(Book)