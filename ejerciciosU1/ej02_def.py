#1.2 => recibe horas y coste y retorna el importe total.
def tiempo(horas, coste):  
    resultado= horas * coste
    return resultado

h = int (input ("Dime cuantas horas has trabajado: "))
c = float(input("Cuanto te pagaban esas horas: "))
print(tiempo(h, c))
