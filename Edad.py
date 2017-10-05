#Eduardo Leyva
class Edad():
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def obtener_edad(self, num1):
        if num1 < 0:
            self.resultado = 'No existes'
        elif num1 < 13:
            self.resultado = 'Eres ninio'
        elif num1 < 18:
            self.resultado = 'Eres adolescente'
        elif num1 < 65:
            self.resultado = 'Eres adulto'
        elif num1 < 120:
            self.resultado = 'Eres adulto mayor'
        else:
            self.resultado = 'Eres Mumm-Ra'