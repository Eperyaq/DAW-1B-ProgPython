"""
inicio
    escribe "dame un numero"
    lee num()
    escribe "dame otro numero"
    lee num2()
    si num==num2 entonces
        muestra "error, los dos numeros no pueden ser iguales"
    sino
        si num>num2 entonces
            dif= num2-num1
            muestra "el " num2  "es menor y entre ellos existen" dif "numeros enteros" 
    sino 
        dif= num1-num2    
        "el " num  "es menor y entre ellos existen" "numeros enteros" 
fin
"""
n=int(input("Dame un numero: "))
m=int(input("Dame un otro numero: "))
med=n-m
if n==m: 
    dif= m-n
    print("Error, los numeros no pueden ser iguales.")
elif n < m: 
    dif=n-m
    print("El numero" , n, "es menor que", m, "y hay",med,"numero entre medio")
else:
    print("el numero",m, "es menor que" ,n, )
