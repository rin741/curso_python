import random

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")

anos = int(input("ingrese su antiguedad laboral: "))

bono = anos*12000

grupo=random.randint(1,100)

if grupo >=1 or grupo <=25:
    print(nombre + apellido)
    print("su bono por antiguedad es: "+str(bono))
    print("usted fue asignado al grupo: A")

elif grupo >=26 or grupo <=50:
    print(nombre + apellido)
    print("su bono por antiguedad es: "+str(bono))
    print("usted fue asignado al grupo: B")

elif grupo >=51 or grupo <=75:
    print(nombre + apellido)
    print("su bono por antiguedad es: "+str(bono))
    print("usted fue asignado al grupo: C")

else:
    print(nombre + apellido)
    print("su bono por antiguedad es: "+str(bono))
    print("usted fue asignado al grupo: D")






