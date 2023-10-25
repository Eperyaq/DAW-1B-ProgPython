def renta ():
    if renta<10000:
        print("Te corresponde un 5% de impositivo.")
    elif renta>10000 and renta<20000:
        print("Te corresponde un 15% de impositivo.")
    elif renta>20000 and renta<35000:
        print("Te corresponde un 20% de impositivo.")
    elif renta>35000 and renta<60000:
        print("Te corresponde un 30% de impositivo.")
    elif renta>60000:
        print("Te corresponde un 45% de impositivo.")


#renta = int(input("Cuanto es tu renta anual?: "))
