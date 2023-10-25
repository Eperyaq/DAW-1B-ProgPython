def tributar (edad, dinero):
    if edad<16 or dinero<1000:
        print("No debes tributar todavia")
    else:
        print("Ya puedes tributar")
    

print(tributar(16,2000))

"""
edad = int(input("Dime tu edad: "))
dinero = int(input("Cuanto dinero cobras mensualmente: "))
"""