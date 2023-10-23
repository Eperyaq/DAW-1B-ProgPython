#5 Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
def impIva():
    precio = int(input("Dime el precio del articulo: "))
    iva= float(input("Dime el % de iva: "))
    if (iva<0 or iva>100):
        print("El porcentaje de iva deber ser entre 1 y 100")
    else:
        print(precio + (precio * iva/100))
    return 
    

print (impIva())