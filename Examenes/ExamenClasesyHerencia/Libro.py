from Material import Material

class Libro(Material):
    
    def __init__(self, id, titulo, autor, anyoPublicacion,genero, numPaginas):
        super().__init__(id, titulo, autor, anyoPublicacion)
        self.genero = genero
        self.numPaginas = numPaginas

    def imprime(self):
        return f"ID: {self._id}, Titulo:{self._titulo}, Autor:{self._autor}, Año:{self._anyoPublicacion}, Genero: {self.genero}, Numero de paginas: {self.numPaginas}"

    # Getter
    # Devuelve el numero de paginas de un libro
    def get_NumPaginas(self):
        return self.numPaginas