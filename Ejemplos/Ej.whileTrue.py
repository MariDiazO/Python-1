'''
Se tiene la siguiente lista de números:
numeros = [3, 5, 2, 8, 1, 10]
Calcular la suma de todos los números de la lista utilizando un bucle while.
'''
numeros = [3, 5, 2, 8, 1, 10]
i = 0
suma = 0

while i < len(numeros):
    suma = suma + numeros[i] #numeros[i] es el valor(numero) que corresponde al índice i (0,1,2,3...)
    #suma += numeros[i] es lo mismo que enunciado arriba
    i += 1
    
print(f"La suma de los números es {suma}") #f = formato