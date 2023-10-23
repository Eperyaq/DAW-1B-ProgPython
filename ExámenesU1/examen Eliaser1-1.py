"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio
    escribe "Dime un numero y te dire si es par o impar"
    lee num
    si (num<0 or num>10) entonces
        escribe "ERROR, el numero no puede ser ni negativo ni mayor que diez"
    sino
        si (num==1 or num==3 or num==5 or num==7 or num==9) entonces
            escribe "Es impar"
        sino
            escribe "Es par" 
Fin
"""
"""
CORRECCIÓN EXAMEN

Inicio
    escribe "Dime un numero y te dire si es par o impar"
    lee num
    si (num<0 or num>10) entonces
        escribe "ERROR, el numero no puede ser ni negativo ni mayor que diez"
    sino
        si (num % 2==0) entonces
            escribe "Es par"
        sino
            escribe "Es impar" 
Fin


"""
