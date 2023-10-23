def factorial(num: int):
    
    total=1
    while(num>1):
        total *= num
        num = num -  1
        
    return total

def factorialStr(num):
    total=1
    res= str(num) +"!=>" + str(num)

    while(num>0):
        res += str(num)
        if (num!=1):
            res+="x"
        total *= num
        num = num -  1
        
    
        
    return res

    return 


numero=int(input("Dime el numero: "))
#print("el factorial de 4!es" +str(factorial(numero)))
print(factorialStr(numero))