#Ejercicio 1.31 - Lee un número hasta que el número esté en el rango 1-10
n=int(input("Intenta adivinar el numero: "))
while (n<1 or n>10) :
    n=int(input("Incorrecto, prueba de nuevo!: "))
print("Acertaste!")
