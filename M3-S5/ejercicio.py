"""Realizar la ejecución de un menú utilizando el lenguaje Python,
donde se le indiquen varias opciones a seleccionar por el usuario y una opción para salir del menú.
Utilizar ciclos y estructuras condicionales."""


import re   #importar libreria para expresiones regulares
opcion = ""
patron = re.compile("^[1-5]{1}$")   #compilacion de patron

while opcion !="5":
    print("Hola Bienvenido! \n Menú:")
    print("1.- Opción 1")
    print("2.- Opción 2")
    print("3.- Opción 3")
    print("4.- Opción 4")
    print("5.- Salir")
    print("Ingrese una opción:")
    
    opcion= input() #leyendo la opción
    if re.match(patron,opcion):
    #evaluamos el input
        if opcion == "1":
            print("Ha elegido la opción 1")
        elif opcion =="2":
            print("Ha elegido la opción 2")
        elif opcion =="3":
            print("Ha elegido la opción 3")
        elif opcion =="4":
            print("Ha elegido la opción 4")
        else:
            print("Ingrese una opción válida")
    else: 
        print("Ha ingresado una opcion incorrecta, valide el ingreso")