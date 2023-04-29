'''Tenemos una lista de números [3, 5, 2, 8, 1, 10]
Se requiere encontrar el primer número par en la lista utilizando un bucle while. '''
lista = [3,5,8,10,1,11]

i = 0
lista_pares = []

while i < len(lista):
    if lista[i] %2 == 0: 
        print("El primer número par es ", lista[i]) # i dentro de la lista
        print("El índice es", i)
        lista_pares.append(lista[i]) #append añade un elemento a la lista
    i = i+1
else:
    print("No hay numero par en la lista")

print(lista_pares)
