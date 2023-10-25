def nivel():
    if nivel==0.0:
        print("te corresponde ", 2400*0.0, "€")
    elif nivel==0.4:
        print("te corresponde ", 2400 * 0.4, "€")
    elif nivel==0.6:
        print("te corresponde ", 2400 * 0.6, "€")
    elif nivel> 0.6:
        print("te corresponde ", 2400 * nivel, "€")
    

#nivel = float(input("Que nivel tienes 0.0, 0.4, 0.6 o más? "))