'''
Pide el tipo de mascota:
---- perro
---- gato
---- conejo
Luego muestra una recomendación de alimento según el animal.
Practica: comparaciones con texto
'''

from funciones import *
import unicodedata

def eliminar_tildes(texto):
    texto_sin_tilde = unicodedata.normalize('NFD', texto)
    return "".join(c for c in texto_sin_tilde if not unicodedata.combining(c))

bienvenidoa("la tienda de mascotas RIWI!")
mascota = eliminar_tildes(inputUsuario("Que tipo de mascota tiene?:\nPerro\nGato\nConejo\n\n","word", "Solo se permite una palabra sin signos, espacios o numeros").strip().upper())
if mascota == "PERRO":
    print("Le recomendamos darle ChowChow!")
elif mascota == "GATO":
    print("Le recomendamos darle MeawMeaw!")
elif mascota == "CONEJO":
    print("Le recomendamos darle Squikers!")
else:
    print("No aceptamos esa especie de mascota")