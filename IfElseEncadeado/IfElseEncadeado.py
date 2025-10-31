"""
ang1 = int(input("Insira o angulo 1: "))
ang2 = int(input("Insira o angulo 2: "))
ang3 = int(input("Insira o angulo 3: "))
if ang1 + ang2 + ang3 != 180:
    print("Ultrapassou 180 graus.")
else:
    if ang1 < 90 and ang2 < 90 and ang3 < 90:
        print("Eh um triangulo acutangulo.")
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        print("Eh um triangulo retangulo.")
    if ang1 > 90 or ang2 > 90 or ang3 > 90:
        print("Eh um angulo obtuso.")
"""
"""
num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
num3 = int(input("Insira outro número: "))

if num1 > num2:
    if num1 > num3:
        maior = num1
    else:
        maior = num3
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3

if num1 < num2:
    if num1 < num3:
        menor = num1
    else:
        menor = num3
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

print(f"O maior número é {maior} e o menor número é {menor}.")
"""
"""
nivel = input("Insira seu nivel de engajamento: ").lower()
valor = float(input("Insira o valor da compra: "))
if nivel not in ["seguidor", "comentarista", "fã"] or valor <= 100:
    print("Nao tem direito ao desconto.")
else:
    if nivel == "seguidor":
        desconto = valor * 0.05
        valorfinal = valor - desconto
        print(f"Valor final eh de {valorfinal}, seu desconto foi de 5%")
    if nivel == "comentarista":
        desconto = valor * 0.08
        valorfinal = valor - desconto
        print(f"Valor final eh de {valorfinal}, seu desconto foi de 8%")
    if nivel == "fã":
        desconto = valor * 0.12
        valorfinal = valor - desconto
        print(f"Valor final eh de {valorfinal}, seu desconto foi de 12%")
"""
"""
medida = input("Informe uma unidade de medida: ").lower()
temperatura = float(input("Insira a temperatura: "))

if medida not in ["celsius", "fahrenheit", "kelvin"]:
    print("Insira uma unidade de medida correta.")
else:
    if medida == "celsius":
        to_kelvin = temperatura + 273
        to_fahr = (temperatura * 1.8) + 32
        print(f"Kelvin: {to_kelvin}. Fahrenheit: {to_fahr}")
    if medida == "fahrenheit":
        to_celsius = (temperatura - 32) / 1,8
        to_kelvin = ((temperatura - 32) / 1,8) + 273
        print(f"Celsius: {to_celsius}. Kelvin: {to_kelvin}")
    if medida == "kelvin":
        to_celsius = temperatura - 273
        to_fahr = ((temperatura - 273) * 1.8) + 32
        print(f"Celsius: {to_celsius}. Fahrenheit: {to_fahr}")
"""
"""
lado1 = float(input("Insira o primeiro lado: "))
lado2 = float(input("Insira o segundo lado: "))
lado3 = float(input("Insira o terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Não se pode usar números negativos ou zero.")
elif not (abs(lado2 - lado3) < lado1 < lado2 + lado3 and
          abs(lado1 - lado3) < lado2 < lado1 + lado3 and
          abs(lado1 - lado2) < lado3 < lado1 + lado2):
    print("Os lados informados não formam um triângulo.")
else:
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
"""
"""
pressao = float(input("Insira a pressao: "))
temperatura = float(input("Insira a temperatura: "))

if pressao not in [100, 200, 300, 400, 500]:     
    print("Os valores informados nao constam no banco de dados.")
else:
    if pressao == 100 and temperatura < 0:
        print("Esta em estado solido.")
    elif pressao == 100 and temperatura == 0:
        print("Esta em estado solido liquido.")
    elif pressao == 100 and 0 < temperatura < 100:
        print("Esta em estado liquido.")
    elif pressao == 100 and temperatura == 100:
        print("Esta em estado liquido vapor.")
    elif pressao == 100 and temperatura > 100:
        print("Esta em estado gasoso.")
    elif pressao == 200 and temperatura == 120:
        print("Esta em mistura liquido vapor.")
    elif pressao == 200 and temperatura > 120:
        print("Esta em estado gasoso.")
    elif pressao == 300 and temperatura == 133.6:
        print("Esta em mistura liquido vapor.")
    elif pressao == 300 and temperatura > 133.6:
        print("Esta em estado gasoso.")
    elif pressao == 400 and temperatura == 143.6:
        print("Esta em mistura liquido vapor.")
    elif pressao == 400 and temperatura > 143.6:
        print("Esta em estado gasoso.")
    elif pressao == 500 and temperatura == 151.9:
        print("Esta em mistura liquido vapor.")
    elif pressao == 500 and temperatura > 151.9:
        print("Esta em estado gasoso")
"""