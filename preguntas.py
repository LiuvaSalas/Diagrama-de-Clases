from alternativas import Alternativa

class Preguntas:
    def __init__(self, enunciado: str, requerida: None, ayuda = None):
        self.enunciado = enunciado
        self.requerida = requerida
        self.ayuda = ayuda
        self.alternativas = []

    @property
    def enunciado(self):
        return self._enunciado

    @property
    def requerida(self):
        return self._requerida

    @property
    def ayuda(self):
        return self._ayuda

    @enunciado.setter
    def enunciado(self, nuevo_enunciado):
        self._enunciado = nuevo_enunciado

    @requerida.setter
    def requerida(self, nuevo_requerida):
        self._requerida = nuevo_requerida

    @ayuda.setter
    def ayuda(self, nuevo_ayuda):
        self._ayuda = nuevo_ayuda


    def agregar_alternativas(self, alternativa):
        self.alternativas.append(alternativa)

    def mostrar(self):
        alternativa_mostrada = "\n".join([alt.mostrar() for alt in self.alternativas])
        return f"{self.enunciado}\n{self.ayuda if self.ayuda else ''}\nAlternativas:\n{alternativa_mostrada}"
