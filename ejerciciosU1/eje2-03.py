"""
Inicio
    escribe "dame un numero inicial"
    lee inicial
    escribe "dime el incremento, es decir, de cuanto en cuanto va la serie"
    lee incremento
    escribe "dime numero final de serie"
    lee serie
    contador=1
    si (incremento <= 0) or (total <= 0) entonces
        escribe "error, no me puedes dar cero en el incremento ni en el total."
    mientras (contador < serie) hacer
        inicial = inicial + incremento
    si (contador==serie -1) entonces
        escribe inicial
    si (contador==serie -2) entonces
        escribe inicial
    sino
        escribe inicial
    contador = contador + 1
        
"""

inicial = int(input("Dime un numero inicial: "))
incremento = int(input("Dime el incremento, es decir, de cuanto en cuanto va la serie: "))
serie = int(input("Dime el numero de dígitos que quieres que tenga la serie: "))
contador = 1

if (incremento<=0) or (serie<=0):
    print("ERROR, no puedes darme cero en el incremento ni en la serie")
else:
    print(f"SERIE => {inicial}-"  , end="")
    while (contador< serie):
        inicial= inicial + incremento
        if contador==serie -1:
            print(f"-{inicial}")
        elif contador == serie -2 :
            print(inicial, end="")
        else :
            print(inicial, end=".." )
        contador = contador+1
        
       
       