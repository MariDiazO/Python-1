'''De la siguiente lista de precios de productos
calcular el precio total de la compra con un 10% de descuento'''

compra = [25.50, 12.30, 36.40, 9.75, 15.20]

print(f"El total es $ {sum(compra)}") #funcion "sum" suma los elementos de la lista
print(f"El total con 10% de desc. es $ {sum(compra)* 0.90}")