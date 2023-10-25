vegetariano = input("Quieres la pizza de tipo vegetariano? si/no ")
if vegetariano=="si":
    ingrediente = print(input("ingredientes: tomate, mozarella y debes escoger si quieres pimiento o tofu. "))
    if ingrediente=="pimiento":
        print("Tu pizza va a llevar tomate, mozarella y pimiento")
    else:
        print("Tu pizza va a llevar tomate, mozarella y tofu")
elif vegetariano=="no":
        ingrediente = print(input("ingredientes: tomate, mozarella y debes escoger si quieres peperoni, jamon, salmon. "))
        if ingrediente=="peperoni":
            print("Tu pizza va a llevar tomate, mozarella y peperoni.")
        elif ingrediente=="jamon":
            print("Tu pizza va a llevar tomate, mozarella y jamon.")
        else: 
            print("Tu pizza va a llevar tomate, mozarella y salmon.")