#24 Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido
precio=(input("Dime cuanto vale: "))
precio2=str(precio).split(".")
print("Cuesta " , precio[0] , " euros y " ,precio[2], "céntimos")