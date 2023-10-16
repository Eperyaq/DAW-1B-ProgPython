#Ejercicio 1.36 - Calcula la media de las notas de un curso.
media=0
cont=1

total=int(input("Cuantas notas vas a introducir?: "))
if (total<0 or total>100):
    print("ERROR, el numero de notas debe estar comprendido entre 1 y 100.")
else:
    while (cont<=total):
        notas=float(input("Dime la notas: "))
        media= media + notas
        cont= cont + 1
    media= media/total
    print("la nota media es: {:.2f}".format(media))
