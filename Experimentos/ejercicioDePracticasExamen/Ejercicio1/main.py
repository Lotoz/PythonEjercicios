from Curso import Curso
from Alumno import Alumno
from Profesor import Profesor

def menu() -> None:
    print("MENÚ DE OPCIONES:")
    print("1. Crear un alumno")
    print("2. Crear un profesor")
    print("3. Crear un curso")
    print("4. Asignar un profesor a un curso")
    print("5. Matricular un alumno en un curso")
    print("6. Mostrar todos los alumnos")
    print("7. Mostrar todos los profesores")
    print("8. Mostrar todos los cursos con sus alumnos y profesor")
    print("9. Evaluar a un alumno en un curso")
    print("10. Eliminar un alumno")
    print("11. Eliminar un curso")
    print("12. Salir del programa")

def seleccionar_opcion() -> int:
    while True:
        try:
            opcion = int(input("Seleccione una opción del menú: "))
            if 1 <= opcion <= 12:  # rango válido
                return opcion
            else:
                print("Debe indicar una opción válida.")
        except ValueError:
            print("Debe introducir un número entero.")

def main() -> None:
    alumnos = dict()
    profesores = dict()
    cursos = dict()
    menu()
    while True:
        opcion = seleccionar_opcion()
        match opcion:
            case 1:
                nombre = input("Introduzca el nombre del alumno: ")
                email = input("Introduzca el email del alumno: ")
                try:
                    edad = int(input("Introduzca la edad del alumno: "))
                except ValueError:
                    print("Debe introducir un número entero.")
                nivel = input("Introduzca el nivel de conocimientos del alumno: ")
                try:
                    alum1 = Alumno.Alumno(nombre, email, edad, nivel)
                    alumnos[alum1.getId()] = alum1
                    print(f"Alumno {alum1.getNombre()} registrado en el sistema")
                except ValueError as e:
                    print(e)
            case 2:
                nombre = input("Introduzca el nombre del profesor: ")
                email = input("Introduzca el email del profesor: ")
                especialidad = input("Introduzca la especialidad del profesor: ")
                try:
                    experiencia = int(input("Introduzca los años de experiencia del profesor: "))
                except ValueError:
                    print("Debe introducir un número entero.")
                try:
                    prof1 = Profesor.Profesor(nombre, email, especialidad,experiencia)
                    profesores[prof1.getId()] = prof1
                    print(f"Profesor {prof1.getNombre()} registrado en el sistema")
                except ValueError as e:
                    print(e)
            case 3:
                codigo = input("Introduzca el código del curso: ")
                nombre = input("Introduzca el nombre del curso: ")
                try:
                    numMaxAlumnos = int(input("Introduzca el nº máximo de alumnos matriculados en el curso: "))
                except ValueError:
                    print("Debe introducir un número entero.")
                try:
                    curso1 = Curso.Curso(codigo, nombre, numMaxAlumnos)
                    cursos[curso1.getCodCurso()] = curso1
                    print(f"Curso {curso1.getNombre()} registrado en el sistema")
                except ValueError as e:
                    print(e)
            case 4:
                codCurso = input("Introduce el código del curso donde vas a asignar al profesor:")
                if codCurso not in cursos:
                    print("Error, ese curso no está registrado en el sistema")
                else:
                    try:
                        idProf = int(input("Indique el id del tutor: "))
                    except ValueError:
                        print("Debe introducir un número entero.")
                    if idProf not in profesores:
                        print("Error, profesor no registrado en el sistema")
                    else: 
                        try:
                            cursos[codCurso].setTutor(profesores[idProf])
                            print(f"Profesor {profesores[idProf].getNombre()} asignado a curso {cursos[codCurso].getNombre()}")
                        except TypeError as e:
                            print(e)
            case 5:
                try:
                    idAlum = int(input("Introduzca el id del alumno a matricular: "))
                except ValueError:
                    print("Debe introducir un número entero.")
                if idAlum not in alumnos:
                    print("Error, alumno no registrado en el sistema")
                else:
                    codCurso = input("Introduzca el código del curso:")
                    if codCurso not in cursos: 
                        print("Error, ese curso no está registrado en el sistema")
                    else:
                        try:
                            cursos[codCurso].matricularAlumno(alumnos[idAlum])
                            print(f"Alumno {alumnos[idAlum].getNombre()} matriculado con éxito en el curso {cursos[codCurso].getNombre()}")
                        except ValueError as e:
                            print(e)
            case 6:
                if len(alumnos) == 0:
                    print("No hay alumnos registrados")
                else:
                    print("Alumnos registrados:\n" + "\n".join(str(alumno) for alumno in alumnos.values()))
            case 7:
                if len(profesores) == 0:
                    print("No hay profesores registrados")
                else:
                    print("Profesores registrados: \n" + "\n".join(str(profe) for profe in profesores.values()))
            case 8:
                if len(cursos) == 0:
                    print("No hay cursos registrados")
                else:
                    print("Cursos registrados: \n" + "\n".join(str(curso) for curso in cursos.values()))
            case 9:
                try:
                    idAlum = int(input("Introduzca el id del alumno a evaluar: "))
                except ValueError:
                    print("Debe introducir un número entero.")
                if idAlum not in alumnos:
                    print("Error, alumno no registrado en el sistema")
                else:
                    codCurso = input("Introduzca el código del curso: ")
                    if codCurso not in cursos: 
                        print("Error, ese curso no está registrado en el sistema")
                    elif alumnos[idAlum] not in cursos[codCurso].getMatriculados():
                        print("Error, ese alumno no está matriculado en el curso")
                    else:
                        try:
                            nota = float(input("Introduzca la nota del alumnno: "))
                        except ValueError:
                            print("Debe introducir un número.")
                        try:
                            cursos[codCurso].evaluarAlumno(alumnos[idAlum],nota)
                            print(f"Evaluación de {alumnos[idAlum].getNombre()} completada")
                        except ValueError as e:
                            print(e)
            case 10:
                try:
                    idAlum = int(input("Introduzca el id del alumno a eliminar: "))
                except ValueError:
                    print("Debe introducir un número entero.")
                if idAlum not in alumnos:
                    print("Error, alumno no registrado en el sistema")
                else:
                    for curso in cursos.values():
                        if alumnos[idAlum] in curso.getMatriculados():
                            curso.getMatriculados().remove(alumnos[idAlum])
                    alumnos.pop(idAlum)
                    print("Alumno eliminado con éxito")
            case 11:
                codCurso = input("Introduzca el código del curso a eliminar: ")
                if codCurso not in cursos:
                    print("Error, curso no registrado en el sistema")
                else:
                    cursos.pop(codCurso)
                    print("Curso eliminado con éxito")
            case 12:
                print("Finalizando programa...")
                break
        input("Pulse una tecla para continuar:")

main()