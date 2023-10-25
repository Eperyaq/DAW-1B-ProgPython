def contra():
    contraseña="contraseña"
    contra=input("Dime cual crees que es la contraseña: ")
    if contra==contraseña:
        print("coincide!")
    else:
        print("no coincide.")
    return

print(contra())
#sigo sin entender porque pone el none