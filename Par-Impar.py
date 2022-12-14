cont = 3
num = int(input(" Ingrese un Numero: "))
print("Vamos a revisar si ", num, " es par o impar")
while cont > 0:
    print(cont)
    cont = cont - 1

if num % 2 == 0: 
    print("El Numero ", num, " es par" )
else:
    print("El Numero ", num, " es impar")