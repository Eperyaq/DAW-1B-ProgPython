"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 365 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 12 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio
    escribe "Dime los días totales que has trabajado"
    lee dias
    
    mientras(dias<0)
        escribe "ERROR, no me puedes dar dias negativos, dime de verdad cuantos dias has trabajado"
        lee dias
    
    años=dias//365
    dias=dias%365
    meses=dias//30
    dias=dias%30
    
   
    si (años==1) entonces
        escribe "Has trabajado", años,"año,"
    sino
        escribe "Has trabajado", años,"años,"
    si (meses==1) entonces
        escribe meses,"mes,"
    sino 
        escribe  meses,"meses"
    si (dias==1) entonces
        escribe dias,"dia."
    sino 
        escribe dias,"dias."
    
Fin
"""
dias=int(input("Dime los dias totales que has trabajado: "))

while (dias<0):
    dias=int(input("ERROR, no puedes dar dias en negativo,Dime de verdad cuantos dias has trabajado: "))
    
años=dias//365
dias=dias%365
meses=dias//30
dias=dias%30

if (años==1):
    print("Has trabajado ", años,"año,", end=" ")
else:
    print("Has trabajado ", años,"años,", end=" ")
    
if(meses==1):
    print( meses,"mes,", end=" ")
else:
    print( meses,"meses,", end=" ")
    
if (dias==1):
    print( dias,"dia.", end=" ")
else:
    print( dias,"dias.", end=" ")
