#16 Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
PRECIO= 3.49
barras= int(input("Cuantas barras has vendido que no son del dia? "))
descu= (PRECIO - 0.60)
print("El precio de las barras del dia antes es: " , descu, "por tanto las " , barras, " barras te salen a: " ,descu*barras)