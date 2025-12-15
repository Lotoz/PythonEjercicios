from cuenta import Cuenta  
class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad = 0 , bonificacion):
        super().__init__(titular)
        super().__init__(cantidad)
        if verificaBonificacion(bonificacion):
            self._bonificacion = bonificacion

    # Verifica una bonificacion y devuelve si es valida
    def verificaBonificacion(bono):
        if bono > 0 and bono < 100:
            return bono
        else:
            raise NameError('La bonificacion no es valida')