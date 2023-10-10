#20 Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión
numero= input("Dime el numero del telefnno con el formato(+34)" )
contador=numero.split("-")
if len(numero)==16 and numero[0]=="+":
    if len(contador[1])==9:
        print(contador[1])
    else:
        print("formato incorrecto")
print("tu numero es:", numero)