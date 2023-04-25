'''Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
subcondiciones; en su lugar, usar condiciones anidadas.'''

#Importar librería math
import math
#variable global
opcion = ""

#Mensaje
print("Ingrese una opción:")
#input
opcion= input()
#evaluar input
if opcion >="0":
        print("El número ingresado es positivo")
elif opcion <="0":
        print("El número ingresado es negativo")
elif opcion == 2n:
        print("El número ingresado es par")
elif opcion == 2n+1:
        print("El número ingresado es impar")
elif opcion =="0":
        print('El número ingresado es = "0"')
else:
        print("Usted no ha ingresado un número")