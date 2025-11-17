from cuenta import Cuenta
from persona import Persona

per = Persona('Jose', 'Ruiz', 'A121313B', 20)
cuenta = Cuenta(per, 10)

cadena = per.mostrarPersona() + cuenta.mostrar()
print(cadena)