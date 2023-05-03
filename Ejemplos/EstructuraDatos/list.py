'''La listas o arreglos son colecciones de datos
se definen por la funcion list = datos entre corchetes'''
#se pueden declarar de varias formas
list = [1,2,3,4,5,6,7,8] #lista de numeros 1-8, el índice parte del 0 a n-1
una_lista = list () #lista vacía
otra_lista = [] #lista vacía
otra_lista = [31,1.72,"Fulanito","Perez"] #definiendo una lista vacia

#acceder a la longitud o largo de la lista con funcion len()
print("Longitud de lista, ",len(list))
print("Longitud de otra_lista, ",len(otra_lista))

#conocer el tipo de dato
print("El tipo de dato de lista es: ",type(list)) #<class 'list'>

#acceder a los elementos de la lista a traves de su indice
print("Elemento en el indice 0 de la lista: ",list[0]) #indices positivos van desde la primera parte de la lista
print("Elemento en el indice -1 de la lista: ",list[-1]) #indices negativos van desde la ultima parte de la lista

#contar los elementos existentes de la lista con la funcion count() dado un elemento a contar, ej nombre_lista.count(elemento_a_contar)
print("Cantidad de veces que se repite el 1 en la lista: ",list.count(1))

#acceder al indice de un elemento de la otra_lista con la funcion index()
print("Indice del elemento Fulanito en la otra_lista: ",otra_lista.index("Fulanito"))

#desempaquetar elementos de la lista en variables
edad, altura, nombre, apellido = otra_lista
print("Edad: ", edad)
print("Altura: ", altura)
print("Nombre: ", nombre)
print("Apellido: ", apellido)

#crear, insertar, actualizar y eliminar elementos de la lista
#crear un nuevo elemento en la lista con funcion append(), añadir
list.append(7) #[1,2,3,4,5,6,7]
print("La lista es: ",list)

#insertar elemento en la lista con funcion insert(index,elemento_insertar)
list.insert(6,8)
print("La lista es: ",list) #[1, 2, 3, 4, 5, 6, 8, 7]

#actualizar elemento en la lista, nombre_lista[indice_actualizar] = valor_asignar
list[6] = 7
list[7] = 8
#lista[7] = "Arroz"
print("La lista es: ",list) #[1, 2, 3, 4, 5, 6, 7, 8]

#remover el elemento
list.append("Arroz")
print("La lista es: ",list)
list.remove("Arroz")
print("La lista es: ",list)

#algunas funciones de la lista
#count(), len(), index(), insert(), remove(), pop(), sort(), reverse()

#funcion pop(indice) extrae un elemento dado un indice por default extrae el ultimo elemento de la lista con indice -1
list.append(9)
print("La lista es: ",list)
elemento_extraido = list.pop(8)
print("La lista es: ",list)

#funcion sort() ordena los elementos de la lista, reverse=True reverse=False
# otra_lista.sort() #[31,1.72,"Fulanito","Perez"] no permite ordenar listas con varios elementos de diferente tipo
list.sort(reverse=True) 
print("La lista es: ",list) #[8, 7, 6, 5, 4, 3, 2, 1]

#funcion reverse() los ultimos elementos cambian a ser primero y los primero cambian a ser último
list.reverse()
print("La lista es: ",list)