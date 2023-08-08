def esNumero(a):
    try:
        a = int(a)
        return(a)
    except:
        print('No es un numero')

def ingresar_numero():
    global num_1, num_2
    num_1 = int(input("Escribe el primer numero: "))
    num_2 = int(input("Escribe el segundo numero: "))
    if esNumero(num_1) and esNumero(num_2): 
        return(num_1, num_2)

def sumar(num_1,num_2):
    resultado = num_1 + num_2
    print(f'El resultado de la operacion es: {resultado}') 

def restar(a,b):
    resultado = a-b
    print(f'El resultado de la operacion es: {resultado}') 
    
def multiplicacion(a,b):
    resultado = a*b
    print(f'El resultado de la operacion es: {resultado}') 

def division(a,b):
    resultado = a/b
    print(f'El resultado de la operacion es: {resultado}') 

def potencia(a,b):
    resultado = a**b
    print(f'El resultado de la operacion es: {resultado}') 

def radicacion(a,b):
    resultado = a**(1/b)
    print(f'El resultado de la operacion es: {resultado}') 
        
#Primera Solucion
opc = int(input("Calculadora Simple \n Opcion 1 --> Suma \n Opcion 2 --> Resta \n Opcion 3 --> Multiplicacion \n Opcion 4 -->Division \n Opcion 5 -->Potencia \n Opcion 6 -->Radicacion \nElige la opcion: "))

if opc == 1 :
    ingresar_numero()
    sumar(num_1, num_2)
elif opc == 2 :
    ingresar_numero()
    restar(num_1, num_2)
elif opc == 3 :
    ingresar_numero()
    multiplicacion(num_1, num_2)
elif opc == 4 :
    ingresar_numero()
    division(num_1, num_2)
elif opc == 5:
    ingresar_numero()
    potencia(num_1, num_2)
elif opc == 6:
    ingresar_numero()
    radicacion(num_1, num_2)
else:
    print("La opcion seleccionada no es disponible.")

    
"""#Segunda Solucion    
    
ing_num = input("Ingresa la operacion a realizar: ")

print('El Resultado es: ', eval(ing_num))
    """



