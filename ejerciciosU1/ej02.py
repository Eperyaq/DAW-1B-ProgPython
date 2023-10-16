#2.-Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
def tiempo():
    horas = int (input ("Dime cuantas horas has trabajado: "))
    coste = float(input("Cuanto te pagaban esas horas: "))
    resultado= horas * coste
    return resultado

print(tiempo())
