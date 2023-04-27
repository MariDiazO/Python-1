'''Calcular en factorial de un número, asignarlo a una variable y luego imprimirla'''

num = 0

#Ciclo para el ingreso del numero
while True:
    num = int(input("Ingrese un número entero positivo : "))
    if num > 0 : # Si el numero es mayor 0
        break
#La factorial es el resultado de todos los enteros positivos
factorial = 1
i = 1

while True:
    factorial *= i # * declara la multiplocacion y suma
   #= factorial = factorial * i
    i = i + 1 #i += 1
    if i > num :
        break
print(f"El factorial de {num} es {factorial}")