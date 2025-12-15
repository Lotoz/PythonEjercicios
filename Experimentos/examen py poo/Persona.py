from abc import ABC, abstractmethod
import re

class Persona(ABC):
    numPersonas = 0
    def __init__(self , nombre: str, email: str) -> None:
        if nombre == "" or nombre.isspace():
            raise ValueError("Error: el nombre no puede estar vacío")
        elif email == "" or email.isspace() or not re.search(r"^\S+@\S+\.\S+$", email):
            raise ValueError("Error: formato de email no válido")
        
        self.id = Persona.numPersonas
        self.nombre = nombre
        self.email = email
        Persona.numPersonas+=1
    
    def getId(self) -> int:
        return self.id
    
    def setNombre(self, nombre) -> None:
        if nombre == "" or nombre.isspace():
            raise ValueError("Error: el nombre no puede estar vacío")
        self.nombre = nombre

    def getNombre(self) -> str:
        return self.nombre
    
    def setEmail(self, email) -> None:
        if email == "" or email.isspace() or not re.search(r"^\S+@\S+\.\S+$", email):
            raise ValueError("Error: formato de email no válido")
        self.email = email

    def getEmail(self) -> str:
        return self.email
    
    @abstractmethod
    def __str__(self) -> str:
        return(f"ID: {self.getId()}\t"
        f"Nombre: {self.getNombre()}\t"
        f"Email: {self.getEmail()}\t")