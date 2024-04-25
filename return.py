def multiplicar_tres_numeros(num1,num2,num3):
    return num1*num2*num3

def division_dos_numeros(primer_numero,segundo_numero):
    return (primer_numero+segundo_numero)/2

valor1=2
valor2=4
valor3=1

resultado1= multiplicar_tres_numeros(valor1,valor2,valor3)+division_dos_numeros(valor1,valor2)
print(resultado1)

resultado2= division_dos_numeros(multiplicar_tres_numeros(valor1,valor2,valor3),valor2)
print(resultado2)
