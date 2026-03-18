'''
Un gimnasio ofrece clases según la edad:
---- menor de 13 → no puede ingresar
---- de 13 a 17 → clase juvenil
---- de 18 a 59 → clase general
---- 60 o más → clase senior
Pide la edad de una persona y muestra a qué grupo pertenece.
Practica: if, elif, else.
'''
from funciones import inputUsuario

edad = inputUsuario("Ingrese su edad: ", "int", "Solo se permiten numeros enteros positivos.")

if edad < 13:
    print("No puedes ingresar.")
elif edad >= 13 and edad <= 17:
    print("Si puedes entrar. Has sido asignado a la clase juvenil")
elif edad >= 18 and edad <= 59:
    print("Si puedes entrar. Has sido asignado a la clase General")
else:
    print("Si puedes entrar. Has sido asignado a la clase Senior")