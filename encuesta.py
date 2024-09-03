from preguntas import Preguntas

class Encuesta:
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.preguntas = []
        self.listado_respuestas = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_nuevo):
        self._nombre = nombre_nuevo

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def agregar_listado_respuestas(self, listado_respuestas):
        self.listado_respuestas.append(listado_respuestas)

    def mostrar(self):
        preguntas_mostradas = "\n".join([preg.mostrar() for preg in self.preguntas])
        return f"Encuesta: {self.nombre}\nPregunta:\n{preguntas_mostradas}"

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_min: int, edad_max: int):
        super().__init__(nombre)
        self.edad_min = edad_min
        self.edad_max = edad_max

    def agregar_listado_respuestas(self, listado_respuestas):
        if self.edad_min <= listado_respuestas.usuario.edad <= self.edad_max:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            print("Su edad no esta dentro del rango etario permitido para contestar esta encuesta.\nMuchas gracias!")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones = [1, 2, 3, 4, 5]):
        super().__init__(nombre)
        self.regiones = regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.region in self.regiones:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            print("Su region no se encuentra dentro de las regiones permitidas.\nMuchas gracias!")