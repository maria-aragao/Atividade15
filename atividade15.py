# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

c = float(input("Primeiro número:"))
d = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")

if operação == "+":
    resultado = c + d

elif operação == "-":
    resultado = c - d

elif operação == "*":
    resultado = c * d

elif operação == "/":
    resultado = c / d

else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)