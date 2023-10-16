#4.-Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
def farenheit(celsius):
    return (celsius *9 / 5)+32

c1 = float(input("Introduzca la temperatura en grados celsius"))
c2 = float(input("Introduzca la temperatura en grados celsius"))

print("La temperatura en grados Farenheit es {:.2f} ºF ({:.2f}ºC)".format(farenheit(c1), c1))
print("La temperatura en grados Farenheit es {:.2f} ºF ({:.2f}ºC)".format(farenheit(c1), c2))