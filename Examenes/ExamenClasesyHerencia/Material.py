#Clase padre de un material
class Material:

    def __init__(self, id, titulo, autor, anyoPublicacion):
        self._id = id
        self._titulo = titulo 
        self._autor = autor
        self._anyoPublicacion = anyoPublicacion
