import sys
sys.path.append(".")
from src.TablaAsignacion import *

class dni:

    def __init__(self, DNI):
        self.DNI = DNI
        self.tabla = TablaAsignacion()

    def checkLongitud(self):
        return len(self.DNI) == 9

    def checkNumber(self):
        return self.DNI[:-1].isdigit()

    def DNISano(self):
        if self.checkLongitud() and self.checkNumber:
            return True
        else: 
            return False

    def getLetter(self):
        return self.DNI[-1]
    
    def DNINumbers(self):
        return self.DNI[:-1]

    def verifyDni(self):
        if self.DNISano:
            if self.tabla.calcularLetra(self.DNINumbers()) == self.getLetter():
                return True
            else: 
                return False
    

    

        

        

