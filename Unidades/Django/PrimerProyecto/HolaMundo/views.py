from django.http import HttpResponse #Necesario para poder responde al cliente
from django.shortcuts import render, redirect #necesario para que funcione la otra forma de visualizar una vista
#con httpresponde, podemos responder con texto plano o con html
#forma de responder al cliente cuando hace un http
from HolaMundo.models import Author
from HolaMundo.models import Book

def hola_mundo (request): # El request captura las peticiones de los clientes
    return HttpResponse ("<h1>AAA</h1>")
    
#Con esto hemos habilitado una vista, pero hay que además enlazar el proyecto con la aplicación

def home (request): # Pinta una página con render, también hay que darlo de alta en urls.py
    return render(request,'index.html')

def autor_list (request):
    author= Author.objects.all()
    return render(request,'author.html',{'author':author})

def libro_list (request):
    book = Book.objects.all()
    return render(request,'book.html',{'books':book})


from HolaMundo.forms import AutorForm

def autor_create (request):
    if request.method == 'GET':
        return render(request, 'create_autor.html', {'autor_form': AutorForm}) #Si tenemos las páginas
#dentro de alguna carpeta dentro de template, entonces habría que especificar el nombre de la
#carpeta return Ej:render(request, 'nombre_carpeta/create_autor.html')
#Hemos añadido el contexto para pasarlo como parámetro a la página create_autor.html
    if request.method == 'POST':
#Estaremos aqui en esta opción cuando le damos a guardar. Para obtener la información que
#envía el formulario:
# EN request.POST es dónde tenemos toda esa información. De hecho si imprimimos esa variable la
#podemos ver.
        form=AutorForm(data=request.POST)
#Hemos creado una instancia de un form de Django al que le estamos pasando los datos usando la
#variable data, de esta manera entiende que se va a registrar una información (que va a ser un
#d1iccionario)
    if form.is_valid: #Realizará de forma automática las validaciones que se han establecido3 en el modelo
        form.save() #Guarda en la BD. En pocas lineas hemos validado y guardado.
        return redirect ('/autor/') #Hay que importar el redirect en shortcuts. Debe redireccionar
#al listado de autores.
    else:
#Debo volver a crear una instancia del forma para dar la opción de poder escribir otra vez
#los datos, con los mismos datos que ha introducido para que vea qué cual puede ser el error.
        form=AutorForm(data=request.POST)
#return render (request, 'create_autor.html',{'autor_form': AutorForm}) #Es como si fuera un
#GET