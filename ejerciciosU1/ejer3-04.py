# Ejercicio 1.34 - Crea un algoritmo que asigne a una variable el número 3 y después pida un número. Debéis mostrar una serie de 3 en 3 tantos números cómo se hayan leído.
n=3
suma=int(input("Dime cuantos numeros quieres que tenga la serie: "))
contador=0
while (contador<suma):
    print(n, end=" ")
    n= n+3
    contador= contador+1