"""
escribe dime un nombre
lee nom()
mientras nombre=="" hacer
    decir dime tu nombre de verdad
    lee nom()

decir dime una edad
lee edad()
mientras edad<0 o edad>125 hacer
    decir dime edad de verdad
    lee edad()
final=125-edad
decir Tu nombre es nom y tienes edad años, aun te quedan final años  por cumplir
"""

nom=input("Dime un nombre: ")
if (nom==""):
    nombre="desconocido"

edad=int(input("Dime una edad: "))
while edad < 0 or edad > 125 :
    edad = input("Debes decirme tu edad de verdad ")
final = 125 - edad

print("Tu nombre es", nom, "y tienes", edad,  "todavia te quedan", final, "años por vivir")