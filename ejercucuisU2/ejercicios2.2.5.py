invertir = int(input("Dime la cantidad a invertir: "))
interes = float(input("Dime el interes anual: "))
años = int(input("Dime los años: "))
#se podria poner float en años? 1.5 años pero 1.7 años no tiene logica
invertir *= 1+ interes/100
invertir= invertir*años
print(invertir)