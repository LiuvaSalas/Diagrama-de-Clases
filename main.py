from usuario import Usuario
from alternativas import Alternativa
from preguntas import Preguntas
from encuesta import (Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion)

def main():
    usuario = input("Indica tu nombre:\n> ")
    numero = 0
    edad = int(input("Indica tu edad:\n> "))
    print("Region:\n1. Tarapaca\n2. Antofagasta\n3. Atacama\n4.Coquimbo\n5.Valparaiso")
    region = int(input("Indica tu region, por favor:\n> "))

    usuario = Usuario(usuario, edad, region)

    #creamos alternativas para probar
    alternativa1 = Alternativa("1. Si")
    alternativa2 = Alternativa("2. No", "Esto significa que no te gustan las toras")

    #creamos preguntas para probar
    pregunta1 = Preguntas("¿Te gustan las tortas?", "Escoge 1, si te gustan las tortas, y 2 si no te gustan")
    pregunta1.agregar_alternativas(alternativa1)
    pregunta1.agregar_alternativas(alternativa2)

    #creamos una encuesta
    encuesta = EncuestaLimitadaEdad("Catacion de Tortas", 18, 30)
    encuesta.agregar_pregunta(pregunta1)

    #mostramos la encuesta
    print(encuesta.mostrar())

    respuesta_usuario = int(input("Responde indicando el numero de la respuesta:\n> "))
    usuario.contestar_encuesta(encuesta, respuesta_usuario)

    print("Muchas gracias por participar\nHasta la proxima!")


main()