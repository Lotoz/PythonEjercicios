from cuenta import Cuenta  
class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad = 0 , bonificacion):
        super().__init__(titular)
        super().__init__(cantidad)
        self._bonificacion = bonificacion