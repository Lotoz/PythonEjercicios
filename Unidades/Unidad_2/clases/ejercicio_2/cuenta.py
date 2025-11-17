class Cuenta:
    
    def __init__(self, titular, cantidad = 0):
        self._titular = titular
        self._cantidad = cantidad
        
    def get_titular(self):
        return self._titular
    
    def get_cantidad(self):
        return self._cantidad
    
    def set_titular(self, newTitular):
        self._titular = newTitular
        
    def set_cantidad(self, newCantidad):
        self._cantidad = newCantidad
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad = self._cantidad + cantidad
        else:
            print(f'No se puede agregar cantidades negativas')
    
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad < self._cantidad:
                self._cantidad = self._cantidad - cantidad
            else:
                print(f'El saldo no es suficiente para esta operacion')
        else:
            print(f'No se puede quitar cantidades negativas')
        
    def mostrar(self):
        return  '\n' + '*Cantidad = ' + self._cantidad
