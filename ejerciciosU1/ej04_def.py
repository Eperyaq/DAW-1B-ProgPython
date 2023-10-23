#1.4 => NO recibe parámetros y retorna la temperatura convertida en grados Farenheit. Dentro de la función se pedirá al usuario los grados Celsius.
def farenheit():
    c1 = float(input("Introduzca la temperatura en grados celsius: "))
    return (c1 *9 / 5)+32




print("La temperatura convertida es: ", farenheit())