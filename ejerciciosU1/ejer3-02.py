#Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...
#preguntar en clase
x=int(input("Dame un numero: "))
y=int(input("Dame otro numero: "))

if (x <= y):
    numini = x
    numfin = y 
else:
    numini = y
    numfin = x

while (numini <= numfin):
    print(numini , end="")
    if (numini != numfin):
        print("-" , end="")
    numini+=1