from django import forms
from HolaMundo.models import Author # importamos el modelo que nos hace falta, en este caso
#necestimos insertar autores
#Creamos nuestro primer Form
class AutorForm (forms.ModelForm): #Vamos a crear un formulario de Django , basado en un
#modelo, por eso hacemos la herencia
#Los forms de django tienen su clase meta, dónde indicamos el modelo al cual hacemos
#referencia.
#Con estas dos clases lo que estamos diciendo es que Django debe crearnos un form que haga
#referencia el modelo author
    class Meta:
        model=Author
#Luego hay que decirle qué campos queremos que tome de este modelo. A veces el modelo
#tiene muchos campos pero sin embargo no hace falta introducirlos todos. Podemos colocar una
#lista de los campos que aparezcan. También existe la opción de poner '__all__',
# fields= ('name','last_name') #En esta caso especificamos los campos que queramos que
#aparezcan en el form.
#En nuestro caso como solo tenemos tres campos vamos a ponerlos todos:
        fields='__all__'