import random
intentos = 10
num_aleatorio = int(random.randint(1,100))
print("Adivina el numero de 1 - 100")

while intentos > 0:
    num_ingresado = int(input("Ingresa el un numero: "))
    if num_ingresado == num_aleatorio:
        print("Lo Adivinaste ! El numero ",num_ingresado, "es el correcto")
    else:
        if num_ingresado > num_aleatorio:
            print("El numero ingresado es mayor, prueba nuevamente.")
            intentos = intentos - 1
            print("Te quedan ",intentos," intentos" )
        else:
            print("El numero ingresado es menor, prueba nuevamente.")
            intentos = intentos - 1
            print("Te quedan ",intentos," intentos" )
    if intentos == 0:
        print("No lo lograste el numero era: ", num_aleatorio)
