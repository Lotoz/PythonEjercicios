from Experimentos.ejercicioDePracticasExamen.Ejercicio1.Evaluable import Evaluable
from Experimentos.ejercicioDePracticasExamen.Ejercicio1.Alumno import Alumno
from Experimentos.ejercicioDePracticasExamen.Ejercicio1.Profesor import Profesor

# Excepciones personalizadas
class cursoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Curso(Evaluable):

    def __init__(self, code, nombre, numMaxAlumnos, profesor: Profesor):
        
        self.code = code
        self.nombre = nombre
        self.profesor = profesor # Asignamos el objeto profesor
        
        #  Diccionario de instancia
        # Debe ir dentro del __init__ con 'self'. Si lo pones fuera,
        # todos los cursos compartirían los mismos alumnos.
        self.alumnosDict = {} 

        if numMaxAlumnos > 0:
            self.numMaxAlumnos = numMaxAlumnos
        else:
            raise cursoError('No puede existir un curso con 0 alumnos.')
        

    # Type Hints de Python
    # En Python no se pone 'Clase variable', se usa 'variable: Clase'
    def matricularAlumno(self, alumno: Alumno):
        
        # Lógica y uso de diccionarios
        # Verificamos si hay espacio
        if len(self.alumnosDict) < self.numMaxAlumnos:
            self.alumnosDict[alumno.get_id()] = alumno
            print(f"Alumno {alumno.get_nombre()} matriculado con éxito.")
        else:
            # Es buena práctica avisar si no cabe
            raise cursoError("El curso está lleno, no se puede matricular.")

    def mostrarProfesor(self):
        return f"El profesor es: {self.profesor.get_nombre()}"
    
    def mostrarAlumnos(self):
        print(f"--- Alumnos en {self.nombre} ---")
        for id_alumno, alumno_obj in self.alumnosDict.items():
            # alumno_obj es la instancia de la clase Alumno
            print(f"ID: {id_alumno} - Nombre: {alumno_obj.get_nombre()}")