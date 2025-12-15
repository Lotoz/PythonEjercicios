from Libro import Libro
from Revista import Revista

#class errorFun(Exception):
#    def __init__(self, msg):
#        super().__init__(msg)


#Diccionario de materiales
biblioteca = {}

#Verifica si las cadenas no son vacias
def verificaCadena(msg):
     while True:
        try:
            cadena = input(msg)
            if len(cadena) <= 0 or cadena.isspace():
                raise Exception
            else:
                return cadena
        except Exception:
            print(f"Ingresa un valor valido.")

#Funcion para verificar y pedir un year valido
def verificaYear():
    while True:
        try:
            year = int(input("Ingrese el año de creacion: "))
            if year <= 0: 
                raise ValueError
            else: 
                return year
        except ValueError:
            print(f"Ingrese un año valido.")
        
#Verificar generos disponibles
def verificaGern(): 
    while True:
        try:
            lista = ["Ficción", "No Ficción", "Terror", "Ciencia"]
            print("Tienes la siguiente lista de generos: \n" \
            "1.Ficción \n 2.No Ficción \n 3.Terror \n 4.Ciencia")
            elegido = int(input("Elige uno valido: "))
            return lista[elegido - 1] #Devuelve el item de la lista seleccionado
        except ValueError:
            print("Elija un valor valido.")

#Verifica que sean numeros mayores a 0
def verificaNum(msg):
    while True:
        try:
            num = int(input(msg))
            if num > 0:
                return num
            else:
                raise ValueError
        except ValueError:
            print(f"Has ingresado un numero invalido. Debe ser mayor a cero. Intenta de nuevo.")

#Verifica que sea el mes valido
def verificaMes():
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    while True:
        try:
            mes = int(input("Ingrese el mes numerico(ej: 11 para Noviembre): "))
            if  mes > 12 or mes < 1:
                raise ValueError
            mesTemp = meses[mes - 1]
            if mesTemp in meses:
                return meses[mes-1]
            else:
                raise ValueError
        except ValueError:
            print(f"Ingrese un mes valido, recuerde que debe ser valor numerico.")

def agregarUnMaterial():
    flag = True
    while flag:
        try:
            eleccion = input("Desea generar un libro o una revista? (Libro = 1, Revista = 2)")
            match(eleccion):
                case '1':
                    
                    id = verificaNum("Ingrese la ID del libro: ")
                    #input("Ingrese la ID del libro: ")
                    if id in biblioteca:
                        print("El libro ya existe.")
                        return
                    titulo = verificaCadena("Ingrese su titulo: ")
                    autor = verificaCadena("Ingrese autor: ")
                    year = verificaYear() #Pide el year y no lo devuelve hasta que sea valido
                    genero = verificaGern() # Pide el genero y debe ser de los espeficados
                    numPaginas = verificaNum("Numero de paginas: ") # Pide el numero de paginas y lo verifica
                    libro = Libro(id,titulo,autor,year,genero,numPaginas)
                    biblioteca[id] = libro
                case '2':
                    id = verificaNum("Ingrese la ID de la revista: ")
                    if id in biblioteca:
                        print("La revista ya existe.")
                        return
                    titulo = verificaCadena("Ingrese su titulo: ")
                    autor = verificaCadena("Ingrese autor: ")
                    year = verificaYear() #Pide el year y no lo devuelve hasta que sea valido
                    numEdition = verificaNum("Ingresa el numero de la edicion:") # Verifica la edicion tenga un numero positivo y que no sea 0
                    mes = verificaMes()
                    revista =  Revista(id, titulo, autor, year, numEdition, mes)
                    biblioteca[id] = revista
            #Salimos del bucle    
            flag = False
        except:
            print("Ingrese un valor numerico valido.")

# Impriem todos los materiales por pantalla ordenados
def listarMateriales():
    if not biblioteca: #Si esta vacia no hay nada que mostrar
        print("La biblioteca está vacía.")
        return
    for id in sorted(biblioteca.keys(), key=lambda s: s):
        print(f"{biblioteca[id].imprime()}")

#Busca un material en la bibliteca por ID
def buscarMaterialPorID():
    if not biblioteca: #Si esta vacia no hay nada que buscar
        print("La biblioteca está vacía.")
        return
    buscado = input("Ingrese el id del material a buscar:")
    if buscado in biblioteca:
        print(f"Se ha encontrado: ")
        print(f"{biblioteca[buscado].imprime()}")
    else: 
        print(f"El material no existe.")

#Elimina un material de la biblioteca por ID
def eliminarMaterialPorId():
    if not biblioteca: #Si esta vacia no hay nada que eliminar
        print("La biblioteca está vacía.")
        return 
    buscado = input("Ingrese el ID del material a eliminar: ")
    if buscado in biblioteca:
        del biblioteca[buscado]
        print(f"El material {buscado} eliminado.")
    else:
        print("El material no existe.")

'''
Generar Estadísticas:debe devuelve todos estos valores 
Total de materiales registrados. 
Número de libros y revistas. 
Promedio de páginas para los libros. W
'''
def generarEstadisticas():
    if not biblioteca: #Si esta vacia no hay nada que mostrar
        print("La biblioteca está vacía. No se pueden generar estadisticas.")
        return
    print(f"Se estan generando las estadisticas")
    total = 0
    # Recorre cuantos materiales hay en biblioteca
    for keys in biblioteca:
        total = total + 1
    print(f"En la biblioteca hay en total {total}")
    contadorLibros = 0
    contadorRevistas = 0
    # Revisa si son libros o revistas
    for k,items in biblioteca.items():
        if isinstance(items, Libro):
            contadorLibros = contadorLibros + 1
        else:
            contadorRevistas = contadorRevistas + 1
    print(f"Hay en total. \n Libros : {contadorLibros} \n Revistas: {contadorRevistas}")
    # Calcula el promedio de paginas
    contador = 0
    suma = 0
    for k, items in biblioteca.items():
        if isinstance(items, Libro):
            suma = items.get_NumPaginas() + suma # vamos sumando
            contador = contador + 1 #Suma el contador para calcular el promedio
    # Calculamos promedio
    promedio = suma / contador
    print(f"El promedio de numero de paginas de los libros es de {promedio}")