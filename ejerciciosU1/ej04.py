#4.-Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
tempcelsius = 0
resultado = 0
tempcelsius= int(input("dame la temp a convertir: "))
print(  (tempcelsius * 9/5) + 32, "ºF")