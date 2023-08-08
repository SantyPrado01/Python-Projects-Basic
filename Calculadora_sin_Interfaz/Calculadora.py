"""#Primera Solucion
#opc = int(input("Calculadora Simple \n Opcion 1 --> Suma \n Opcion 2 --> Resta \n Opcion 3 --> Multiplicacion \n Opcion 4 -->Division \n Elige la opcion: "))

#if opc == 1 :
    num_1 = int(input("Escribe el primer numero: "))
    num_2 = int(input("Escribe el segundo numero: "))
    resultado = num_1 + num_2
    print("El resultado de la suma es ", resultado)
elif opc == 2 :
    num_1 = int(input("Escribe el primer numero: "))
    num_2 = int(input("Escribe el segundo numero: "))
    resultado = num_1 - num_2
    print("El resultado de la resta es ", resultado)
elif opc == 3 :
    num_1 = int(input("Escribe el primer numero: "))
    num_2 = int(input("Escribe el segundo numero: "))
    resultado = num_1 * num_2
    print("El resultado de la multiplicacion es ", resultado)
elif opc == 4 :
    num_1 = int(input("Escribe el primer numero: "))
    num_2 = int(input("Escribe el segundo numero: "))
    resultado = num_1 / num_2
    print("El resultado de la division es ", resultado)
else:
    print("La opcion seleccionada no es disponible.")"""

    
"""#Segunda Solucion    
    
ing_num = input("Ingresa la operacion a realizar: ")

print('El Resultado es: ', eval(ing_num))
    """

def esNumero(a):
    try:
        a = int(a)
        return(a)
    except:
        print('No es un numero')


def sumar(a,b):
    if esNumero(a) and esNumero(b): 
        resultado = a + b
        return resultado
    else:
        print('No ingresaste un numero')

def restar(a,b):
    if esNumero(a) and esNumero(b):
        resultado = a-b
        return(resultado)
    else:
        print('No ingresaste un numero')
    
def multiplicacion(a,b):
    if esNumero(a) and esNumero(b):
        resultado = a*b
        return(resultado)
    else:
        print('No ingresaste un numero')

def division(a,b):
    if esNumero(a) and esNumero(b):
        resultado = a/b
        return(resultado)
    else:
        print('No ingresaste un numero')

def potencia(a,b):
    if esNumero(a) and esNumero(b):
        resultado = a**b
        return(resultado)
    else:
        print('No ingresaste un numero')

def radicacion(a,b):
    if esNumero(a) and esNumero(b):
        resultado = a**(1/b)
        print(resultado)
    else:
        print('No ingresaste un numero')

radicacion('q', 2)