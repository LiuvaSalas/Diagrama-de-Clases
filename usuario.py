from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region


    @property
    def correo(self):
        return self._correo

    @property
    def edad(self):
        return self._edad

    @property
    def region(self):
        return self._region
    
    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @region.setter
    def region(self, nueva_region):
        self._region = nueva_region

    def contestar_encuesta(self, encuesta, respuestas):
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado_respuestas)