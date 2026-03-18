'''
Pide la cantidad de clases asistidas por un estudiante en un mes.
Reglas:
--- menos de 5 → asistencia baja
--- entre 5 y 8 → asistencia media
--- 9 o más → asistencia alta
Practica: clasificación por rangos.
'''

import os
from funciones import *

os.system('clear')
bienvenidoa('la academia de baile RIWI!')

asistencias = inputUsuario('Cuantas clases asistio el estudiante?:\n\n','int', 'Solo se admiten numeros enteros positivos')
if asistencias < 5:
    print('El estudiante tiene asistencia baja!')
elif asistencias >= 5 and asistencias <= 8:
    print('El estudiante tiene asistencia media')
if asistencias >= 9:
    print('El estudiante tiene asistencia alta')