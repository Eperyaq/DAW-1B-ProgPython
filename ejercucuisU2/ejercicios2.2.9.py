contra = "contraseña"
pregunta = input("Dime cual crees que es la contraseña: ")
while pregunta != contra:
    if pregunta != contra:
        pregunta=input("Te equivocaste, prueba de nuevo: ")
    
print("Acertaste!!")