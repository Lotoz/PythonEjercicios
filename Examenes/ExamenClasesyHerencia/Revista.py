from Material import Material

class Revista(Material):

    def __init__(self, id, titulo, autor, anyoPublicacion,numEdicion, mes):
        super().__init__(id, titulo, autor, anyoPublicacion)
        self.numEdicion = numEdicion
        self.mes = mes

    def imprime(self):
        return f"ID: {self._id}, Titulo:{self._titulo}, Autor:{self._autor}, Año:{self._anyoPublicacion}, Numero de Edicio: {self.numEdicion}, Mes publicado: {self.mes}"