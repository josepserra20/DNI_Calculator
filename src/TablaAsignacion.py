
class TablaAsignacion:
    
    def __init__(self):
        self.tabla =  [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 
						'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]
        

    def getLetra(self, position):
        try:
            return self.tabla[position]
        except:
            return 'Fuera de rango'

    def calcularLetra(self, DNI):

        position = int(DNI) % len(self.tabla)
        return self.getLetra(position)
