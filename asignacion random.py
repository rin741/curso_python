import random
numero=random.randint(1,3)
nombre_persona=input("ingrese nombre para asignarle un grupo: ")

if numero == 1:
    print(nombre_persona + "fuiste asignado en el grupo A")
elif numero == 2:
    print(nombre_persona + "fuiste asignado en el grupo B")
else:
    print(nombre_persona + "fuiste asignado en el grupo C")
