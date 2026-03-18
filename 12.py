'''
Registrar 5 personas en un gimnasio.
Por cada una pedir:
--- nombre
--- días asistidos en la semana
--- minutos promedio entrenados por día

Clasificar:
--- menos de 3 días → bajo compromiso
--- 3 a 4 días → compromiso medio
--- 5 o más → compromiso alto

Al final mostrar cuántas personas quedaron en cada categoría.
Practica: ciclos, contadores, condicionales.
'''
from funciones import *
import os

os.system('clear')
for i in range(5):
    nombre = inputUsuario(f'Coloque el nombre de la persona #{i+1} ')