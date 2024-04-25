import random

numero_dado=random.randint(1,6)
print("el numero que arrojo el dado fue: "+str(numero_dado))

if numero_dado%2==0:
    print("este numero es un par")
else:
    print("este numero es impar")
