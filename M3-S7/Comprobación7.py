'''Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en
pantalla el valor de cada elemento indicando si es par, impar o cero.'''

#indice parte desde el 0 [0,1,2,3,4,5,6,7,8,9]
#Definimos una lista de numeros del 1 -10
lista = [4,6,2,9,6,0,33,8,2,67]

for i in lista:
    if i == 0:
        print("El numero es 0.")
    elif i % 2 == 0 :
        print(f"El numero {i} es par.")
    else:
        print(f"El numero {i} es impar.")