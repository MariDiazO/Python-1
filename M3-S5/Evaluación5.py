'''Eliminar todas la vocales de la palabra "palelepípedo"'''
'''Imprimir en pantalla las consonantes restantes y su posición de dicha palabra'''

#Variable que contiene "paralelepípedo"
palabra = "paralelepípedo"
consonantes = ""
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

#Para i en un rango (len=length) de largo = palabra (palabra="paralelpípedo")
for i in range(len(palabra)): #range convierte cada uno de los elementos en in ÍNDICE
    #si "paralelepípedo" no contiene vocales
    if palabra[i] not in vocales:
        #Las consonantes son 
        consonantes += palabra[i]
        print(f"La letra{palabra[i]}se encuentra en la posición {i}")
#Imprime las consonantes contenidas en "paralelepípedo"
print(consonantes)