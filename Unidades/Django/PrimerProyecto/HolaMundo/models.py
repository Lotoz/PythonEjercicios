from django.db import models

# Create your models here.
# Aqui habra codigo python
# Al aplicar esta herencia, Django va a saber que Author es una tabla en la BD
# Create your models here.
# Al aplicar esta herencia, Django va sa saber que Author es una tabla en la BD
class Author (models.Model):
    name=models.CharField (verbose_name='Nombre', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    last_name=models.CharField(verbose_name='Apellido',
    max_length=150,
    default='')
    age=models.PositiveSmallIntegerField (verbose_name='Edad',
    )
    age = models.PositiveSmallIntegerField (verbose_name = 'Edad', default = 0)
    mail = models.CharField(verbose_name = 'Correo', max_length = 30)
    nivel = models.CharField(verbose_name="Nivel ingles", max_length= 100 )
    
    def __str__(self):
        return f'{self.name} {self.last_name}'

class Book (models.Model):
    title=models.CharField('Título del libro',max_length=255,unique=True)
    #Unique=True , Django no va a permitir introducir dos libros con títulos iguales. Cuando cree este campo en la BD solo permitir valores diferentes.
    cod=models.CharField('Codigo',max_length=15,unique=True)
    #Cascade ,de esta forma indicamos que cuando se borre un autor en la Bd,también se borrará el libro.
    author=models.ManyToManyField(Author)
    def __str__(self):
        return f'{self.title} {self.cod} {self.author}'
    
