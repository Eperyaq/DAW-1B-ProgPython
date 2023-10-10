#6.-Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
precio = float(input("Dime el precio del articulo: "))
print ("El precio del importe sin iva es: " , precio - precio* 0.10)
print ("Has pagado de iva : " , precio * 0.10)