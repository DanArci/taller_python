'''
En un spa hay estos servicios:
--- masaje
--- facial
--- manicure
Pide al usuario qué servicio desea y muestra un mensaje confirmando
si existe o no.
Practica: condicionales con texto.
'''

from funciones import *
import os
import unicodedata

def eliminar_tildes(texto):
    texto_sin_tilde = unicodedata.normalize('NFD', texto)
    return "".join(c for c in texto_sin_tilde if not unicodedata.combining(c))

os.system('clear')
bienvenidoa("el spa RIWI!")
servicio = eliminar_tildes(inputUsuario("Coloque que servicio quiere recibir:\n\n","phrase","Error.").strip().upper())

if servicio == "MASAJE":
    print("Contamos con ese servicio!")
elif servicio == "FACIAL":
    print("Contamos con ese servicio!")
elif servicio == "MANICURE":
    print("Contamos con ese servicio!")
else:
    print("No contamos con ese servicio :(")