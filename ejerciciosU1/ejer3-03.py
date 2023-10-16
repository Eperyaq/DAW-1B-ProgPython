# Ejercicio 1.33 - Lee 3 números y dame los números ordenados de menor a mayor.
n1 = int(input("Dame el primer numero: "))
n2 = int(input("Dame el segundo numero: "))
n3 = int(input("Dame el tercer numero: "))
if (n1<n2 and n1<n3) :
    if (n2<n3):
        print("tus numeros son: " ,n1,n2,n3)
    else :
        print("tus numeros son: " ,n1,n3,n2)
elif (n2<n1 and n2<n3) :
    if (n1<n3) :
        print("tus numeros son", n2,n1,n3)
    else:
        print("tus numeros son", n2,n3,n1)
elif (n3<n1 and n3<n2) :
    if (n2<n1) :
        print("tus numeros son", n3,n2,n1)
    else:
        print("tus numeros son", n3,n1,n2)

   