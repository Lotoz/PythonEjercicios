from Alumno import Alumno
from Profesor import Profesor
from Evaluable import Evaluable

class Curso(Evaluable):
    def __init__(
        self, 
        codigo: str, 
        nombre: str, 
        numMaxAlumnos: int, 
        
    ) -> None:
        if codigo == "" or codigo.isspace():
            raise ValueError("Error: debe indicar un código de curso correcto")
        elif nombre == "" or nombre.isspace():
            raise ValueError("Error, debe indicar un nombre válido para el curso")
        elif numMaxAlumnos < 1:
            raise ValueError("Error, debe permitirse al menos un alumno en el curso")
        
        self.codigo = codigo
        self.nombre = nombre
        self.numMaxAlumnos = numMaxAlumnos
        self.matriculados: set[Alumno] = set()
        self.tutor: Profesor|None = None
    
    def getMatriculados(self) -> set[Alumno]:
        return self.matriculados
 
    def evaluarAlumno(self, alum: Alumno, evaluacion: float)-> None:
        if alum not in self.getMatriculados():
            raise ValueError(f"Error, el alumno {alum.getNombre()} no se encuentra matriculado")
        elif self.tutor is None:
            raise ValueError("No se puede evaluar a ningún alumno sin un tutor")
        alum.getNota().append(evaluacion)

    def matricularAlumno(self, alum: Alumno) -> None:
        if not isinstance(alum, Alumno):
            raise TypeError("Error, no se está matriculando a un alumno")
        elif len(self.getMatriculados()) >= self.numMaxAlumnos:
            raise ValueError("Error, el curso ya está lleno")
        elif alum in self.getMatriculados():
            raise ValueError("Error, el alumno ya está matriculado")
        self.matriculados.add(alum)

    def getCodCurso(self) -> str:
        return self.codigo
    
    def getNombre(self) -> str:
        return self.nombre
    
    def getNumMaxMatriculados(self) -> int:
        return self.numMaxAlumnos
    
    def getTutor(self) -> Profesor:
        return self.tutor
    
    def setTutor(self, prof: Profesor) -> None:
        if not isinstance(prof, Profesor):
            raise TypeError("Error, eso no es un profesor")
        self.tutor = prof

    def __str__(self):
        return(
            "Curso: \n"
            + f"Código: {self.getCodCurso()} \t"
            + f"Nombre: {self.getNombre()} \t"
            + f"Nº máximo de matriculados: {self.getNumMaxMatriculados()} \t"
            + f"Tutor: {str(self.getTutor()) if self.getTutor() is not None else 'Sin tutor'} \t"
            + "Alumnos matriculados: \n"
            + "\n".join(alum.getNombre() for alum in self.getMatriculados())
        )