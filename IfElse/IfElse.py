"""
import math
cat1 = float(input("Informe o valor do cateto: "))
cat2 = float(input("Informe o outro valor do cateto: "))
if cat1 < 0 or cat2 < 0:
    print("Numero negativo. Nao pode ser feito o calculo.")
else:
    hip = math.sqrt((cat1 ** 2) + (cat2 ** 2))
    print(f"A hipotenusa é {hip}.")
"""
"""
num1 = float(input("Insira um numero: "))
num2 = float(input("Insira outro numero: "))
if num1 > num2:
    print(f"O {num1} é maior que o {num2}")
else:
    print(f"O {num2} é maior que o {num1}")
"""
"""
num = float(input("Insira um numero: "))
if 0 < num < 1:
    print("Esta dentro do intervalo.")
else:
    print("Esta fora do intervalo")
"""
"""
letra = input("Insira uma letra: ").lower()
if letra in "aeiou":
    print("Eh uma vogal.")
else:
    print("Nao eh uma vogal.")
"""
"""
num1 = int(input("Insira um numero: "))
num2 = int(input("Insira outro numero: "))
if num2 % num1 == 0:
    print("Eh multiplo")
else:
    print("Nao eh multiplo.")
"""
"""
valor = float(input("Qual foi o valor da compra: "))
if valor >= 6999.00:
    desconto = valor * 0.15
    valorfinal = valor - desconto
    print(f"O valor final foi de R${valorfinal}")
else:
    desconto = valor * 0.05
    valorfinal = valor - desconto
    print(f"O valor final foi de R${valorfinal}")
"""
"""
num1 = float(input("Insira um numero: "))
num2 = float(input("Insira outro numero: "))
if num1 == num2:
    print("Numero sao iguais.")
else:
    if num1 > num2:
        print(f"{num1} eh maior que {num2}")
    else:
        print(f"{num2} eh maior que {num1}")
"""
"""
altura = float(input("Insira sua altura: "))
idade = int(input("Insira sua idade: "))
horas = int(input("Insira suas horas de voo: "))
peso = float(input("Insira seu peso: "))
if altura >= 1.75 and 22 <= idade <= 40 and horas > 1600 and 65 <= peso <= 95:
    print("Esta apto para ingressar.")
else:
    print("Nao esta apto para ingressar.")
"""
"""
saque = int(input("Quanto voce quer sacar? "))
if saque % 5 != 0:
    print(" Valor indisponível, dirija-se a outro caixa.")
else:
    notas50 = saque // 50
    resto = saque % 50

    notas10 = resto // 10
    resto = resto % 10

    notas5 = resto // 5

    print("Saque realizado com sucesso!")
    print(f"Cédulas de R$50: {notas50}")
    print(f"Cédulas de R$10: {notas10}")
    print(f"Cédulas de R$5: {notas5}")
"""
"""
lado1 = float(input("Insira o lado 1 do triangulo: "))
lado2 = float(input("Insira o lado 2 do triangulo: "))
lado3 = float(input("Insira o lado 3 do triangulo: "))
if lado1 < 0 or lado2 < 0 or lado3 < 0:
    print("Nao eh possivel calcular com valor negativo.")
else:
    if (abs(lado2 - lado3) < lado1 < lado2 + lado3 and
        abs(lado1 - lado3) < lado2 < lado1 + lado3 and
        abs(lado1 - lado2) < lado3 < lado1 + lado2):
        print("É um triângulo.")
    else:
        print("Não é um triângulo.")
"""