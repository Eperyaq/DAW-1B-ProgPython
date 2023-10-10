#12.-Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
peso = float(input("Dime tu peso en kg: "))
altura = float(input("Dime tu altura en metros: "))
imc = peso % (altura*altura)
print("Tu indice de masa corporal es: " , f"{imc:.2f}")