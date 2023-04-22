#Las variables globales se ubican fuera de las estructuras de codigo
variable_global ="Se puede acceder desde todo el documento"

#Las variables locales se ubican dentro de las estructuras
def suma (a,b): #def = definir las variables,
    suma_valores= a+b
    return suma_valores# return = retorna en valor
print(suma(2,1))#Las variables locales son llamadas dentro de su estrucutra de codigo
print(variable_global) #Llamamos la variable global en cualquien momento de la indentacion


#Las funciones en Python se crean usando la palabra clave def, seguida de un nombre de función y parámetros de función entre paréntesis.
#Una función siempre devuelve un valor. La función utiliza la palabra clave return  para devolver un valor; si no desea devolver ningún valor, se devolverá el valor predeterminado None.
#El nombre de la función se usa para llamar a la función, pasando los parámetros necesarios entre paréntesis.
# esta es una función básica de suma

#Ejemplo:
def suma(a, b): #delinimos la funcion suma para realizar una adición.
    return a + b #retorna el valor
result = suma(1, 2)
# result = 3
print(suma) #imprime el resultado de la funcion en consola

