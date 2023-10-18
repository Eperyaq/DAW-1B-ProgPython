"""
Pasa el siguiente algoritmo escrito en pseudocódigo a un programa Python.

El algoritmo pide tus frutas preferidas y sigue leyendo frutas hasta que se introduce un valor vacío. Entonces escribe la lista de frutas favoritas. Si no se introduce ninguna fruta muestra un mensaje indicando que no e gustan las frutas.

*** Ejemplo 1 - el usuario introduce varias frutas:

> Dime tus frutas preferidas:
> plátano
> melón
> naranja
> pera
>
> Lista de frutas favoritas => plátano - melón - naranja - pera.

*** Ejemplo 2 - el usuario no introduce ninguna fruta:

> Dime tus frutas preferidas:
> 
> No te gusta ninguna fruta.
"""

"""
Inicio

    Escribe "Dime tus frutas favoritas: "
    Lee fruta

    Si (fruta == "") entonces
        Escribe "No te gusta ninguna fruta."
    Sino
        lista = ""

        Mientras (fruta != "") hacer
            lista = lista + fruta
            Lee fruta
            Si (fruta != "") entonces
                lista = lista + " - "

        Escribe "Lista de frutas favoritas => " + lista + "."

Fin
"""
lista=""
fruta=str(input("Dime tu fruta favorita: "))
if(fruta==""):
    print("No te gusta ninguna fruta.")
else:
    
    while (fruta!=""):
        lista = lista + fruta
        fruta=input("dime otra: ")
        if (fruta!=""):
            lista= lista + " - "
    print("Lista de frutas favoritas =>", lista, end=".")
#He puesto el end="." porque al concatenarlo todo se quedaba un espacio entre el punto y el objeto de la lista.