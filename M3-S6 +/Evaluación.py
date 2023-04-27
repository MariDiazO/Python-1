'''Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a menor.'''

numeros = input('ingrese 3 numeros distintos separados por coma (,): ') 
numeros = [ int(i) for i in numeros.split(',') ]

def check_length_three(num: list) -> bool: 
    if len(num) == 3: 
        return True 
    else: return False
    +
def check_no_distintos(num: list) -> bool: 
    if num[0] != num[1] and num[0] != num[2] and num[1] != num[2]: 
        return True 
    else: 
        return False
    
def sort_no(num: list) -> list: 
    print(num) 
    return sorted(num)

while check_length_three(numeros) == False or check_no_distintos(numeros) == False:
    numeros = input('Debe ingresar 3 numeros distintos separados por coma (,) :')
    numeros = [ int(i) for i in numeros.split(',') ] 
    # print('numeros seleccionados:', numeros) numeros= sort_no(numeros) print("Los numeros ingresados ordenados de menor a mayor son:") print(*numeros, sep=", ")