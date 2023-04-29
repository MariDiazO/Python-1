'''Usando Bucle For, mostrar el numero de mayor valor en la lista, el menor, el repetido'''

lista = [45, 23, 67, 99, 12, 356, 78, 90, 23, 45, 45, 45]
mayor = lista[0] #numero en la lista
menor = lista[0]
repetido = []

for elemento in lista: #para
    if elemento > mayor: #si elemento es mayor al numero sigue evaluando los numeros de la lista
        mayor = elemento #ahora num tiene el valor del mayor numero encontrado en la lista
    if elemento < menor:
        menor = elemento
    if lista.count(elemento) > 1 and elemento not in repetido : #si la cuenta de la lista es mayor a 1 y el elemento no esta en "repetido"
        repetido.append(elemento)
        print(lista.count(elemento))
        
print(f"El mayor {mayor}")
print(f"El menor {menor}")
print(f"El repetido {repetido}")