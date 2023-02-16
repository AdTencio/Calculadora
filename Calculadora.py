#Funciones que continen las != operaciones.
def sumar(num1, num2):
    resultado = num1 + num2
    return f'El resultado de la operación es: {resultado}'

def restar(num1, num2):
    resultado = num1 - num2
    return f'El resultado de la operación es: {resultado}'

def multiplicar(num1, num2):
    resultado = num1 * num2
    return f'El resultado de la operación es: {resultado}'
    
def dividir(num1, num2):
    if num2 == 0:
        print("No se puede dividir por cero")
    else:
        resultado = num1 / num2
        return f'El resultado de la operación es: {resultado}'


#Funcion que ejecuta la calculadora.
def calculadora ():
    num1 = int(input("Ingresa el primer valor: "))
    num2 = int(input("Ingresa el segundo valor: "))
    print(f'"Para sumar ingrese 1, Para restar ingrese 2, para multplicar ingrese 3, para dividir ingrese 4"')
    operacion_input = int(input())
    if operacion_input == 1:
        print(sumar(num1,num2))
    elif operacion_input == 2:
        print(restar(num1,num2))
    elif operacion_input == 3:
        print(multiplicar(num1,num2))
    elif operacion_input == 4:
        print(dividir(num1,num2))
    else :
        print("no ingresaste un numero valido")
    

calculadora()




