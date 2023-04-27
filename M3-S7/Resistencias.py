# La resistencia dentro de un circuito paralelo se calcula como:
# Rt= 1/((1/R1)+(1/R2)+(1/R3)+(1/Rn))
# Donde:
# RT es la resistencia total
# R1 es la resistencia 1
# R2 es la resistencia 2
# R3 es la resistencia 3
# Rn la n-esima resistencia
# Realiza el codigo en Pyuthon para calcular la resistencia total del circuito
def validate_input_float(texto):
#ingreso de valores    
    while True:
        try:    
            r = float(input(texto)) #float(), str(), int() casteo o transformacion, conversion del tipo de dato            
            if r > 0:
                return r
            else:
                print("El valor es menor a 0")
        except Exception as  e:
            print("Ha ocurrido un error en el ingreso de la resistencia ",e)
            print("Ha ocurrido un error, ingrese de nuevo el valor de la resistencia")      
r_1 = validate_input_float("Ingrese la resistencia 1: ") #llamada a funcion o invocando
r_2 = validate_input_float("Ingrese la resistencia 2: ")
r_3 = validate_input_float("Ingrese la resistencia 3: ")

# calcular la resistencia total
resistencia_total = 1/((1/r_1) + (1/r_2) + (1/r_3))

# imprimir la resistencia total en consola
print("La resistencia total es de", resistencia_total)