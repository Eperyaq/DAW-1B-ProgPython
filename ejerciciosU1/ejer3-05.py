#Ejercicio 1.35 - Pide dos números. Después pide un tercer número del 1 al 4, dependiendo de este número el algoritmo debe hacer lo siguiente:
n=int(input("Dime un numero: "))
m=int(input("Dime otro numero: "))
variable=int(input("Dime otro mas pero del 1 al 4: "))
while (variable<1 or variable>4):
    print("Error, debes darme un numero del 1 al 4")
    variable=int(input("Prueba de nuevo: "))
if (variable == 1):
    print("has escogido sumar" ,n, "+",m,"y el resultado es=", n+m)
elif (variable==2):
    print("has escogido restar" ,n, "-",m,"y el resultado es=", n-m)
elif (variable==3):
    print("has escogido multiplicar" ,n, "x",m,"y el resultado es=", n*m)
else:
    if (m==0 or n==0):
        print("No puedes dividir entre cero!!")
    else:
        print("has escogido dividir" ,n, ":",m,"y el resultado es=", n/m)