#print("123")
#1.-
#print ("Dime tu nombre")
#nombre = input ()
#print ("hola, " + nombre)


#2.-
#print("Cuantas horas has trabajado?")
#horas = int (input ())
#coste = 10
#resultado = horas * coste
#print("Importe total: " , resultado) 

#3.-
#ancho = 17
#alto = 12.0
#print ("1. ancho/2 = " , ancho / 2  )
#print ("2. ancho//2 = " , ((ancho / 2) /2) )
#print ("3. alto/3 = " , alto / 3  )
#print ("4. 1+2*5 = " , 1+2*5 )

#4.-
#tempcelsius = 0
#resultado = 0
#tempcelsius= int(input("dame la temp a convertir: "))
#print(  (tempcelsius * 9/5) + 32)

#precio = 0
#resultado = 0

#5.-
#precio = int(input("Dime el precio del articulo: "))
#print (precio * 0.21)

#6.-
#precio = int(input("Dime el precio del articulo: "))
#print ("El precio del importe sin iva es: " , precio - precio* 0.10)
#print ("Has pagado de iva : " , precio * 0.10)



#7.-
#a=0 
#b=0
#c=0

#print("Dime tres numeros monstro: ")
#a=int(input("dime el primero: "))
#b=int(input("dime el segundo: "))
#c=int(input("dime el tercero: "))
#print(a+b+c)



#numeros=[1,2,3]
#a,b,c= numeros
#print(b)




#2.10
#resultado= pow(((3+2)/(2*5)), 2)
#print(resultado)

#2.11 ¿?
#a=int(input("Dame un numero"))
#suma = (a*(a+1)) /2
#print("La suma es: " , suma)

#for()
#while a<=1 or a>1:
#    resultado=((a*(a+1))/2)
#    break

#print("tu resultado es: " , resultado )
#no se como funciona while en python 

#2.12
#peso = float(input("Dime tu peso en kg: "))
#altura = float(input("Dime tu altura en metros: "))
#imc = peso % (altura*altura)
#print("Tu indice de masa corporal es: " , imc)

#2.13 ¿?
#n = int(input("Dime un numero: "))
#m = int(input("Dime otro: "))
#c = n//m
#r = n%m
#print("La división de" , n , "entre " , m ,  "da un cociente" ,c, "y un resto" ,r,)


#2.14
#payaso=int(input("Cuantos payasos quieres que haya en el pedido?: "))
#muñecas=int(input("Y cuantas muñecas?: "))
#peso=(payaso*112)+(muñecas*75)
#print("El pedido va a pesar: " , peso , "gramos.")

#2.15 ¿?
#dinero=float(input("Cuanto dinero hay en la cuenta?: "))
#interes = dinero * (1+0.04)
#print("ahorros en el primer año= "{intereses:.2})



#2.16

#PRECIO= 3.49

#2.17
#nombre = input("Dime tu nombre: ")
#veces=int(input("Repetir.  cuantas?"))
#print((nombre + "\n") * veces)

#2.18
#nombre=input("Nombre completo: ")
#print(nombre.lower())
#print(nombre.upper())
#print(nombre.title())

#2.19
#usar  len()

#2.20
#numero= input("Dime el numero del telefnno con el formato(+34)" )
#contador=numero.split("-")
#if len(numero)==16 and numero[0]=="+":
    #if len(contador[1])==9:
       # print(contador[1])
    #else:
        #print("formato incorrecto")

#2.21
#m= "hola"
#print(m[::-1])

#2.22
#frase = input("Dime una frase: ")
#vocal= input("Dime una vocal para ponerla en mayusculas: ")
#print(frase.replace(vocal, vocal.upper()))

#2.23
#mail = input("Dime tu correo electronico: ")
#print(mail[:mail.find("@")] + "@ceu.es")

#2.24 mirarlo
#precio=(input("Dime el precio: "))
#precio2=str(precio).split(".")
#print("Cuesta " , precio[0] , " euros y " ,precio[1], "céntimos")


