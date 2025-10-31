"""
limite = int(input("Insira o limite: "))

if limite > 1:
    num = 1  
    while num <= limite:
        print(num)
        num = num + 2  
else:
    print("O número informado deve ser maior que 1.")
"""
"""
begin = 20

while begin >= 0:
    print(begin)
    begin = begin - 1
"""
"""
num = int(input("Insira o numero que quer multiplicar: "))
tab = 1
while tab <= 10:
    print(f"{num} x {tab} = {num * tab}")
    tab = tab + 1
"""
"""
inferior = int(input("Insira o inferior: "))
superior = int(input("Insira o superior: "))
if inferior > superior:
    print("Nao eh possivel calcular.")
else:
    soma = 0
    num = inferior
    while num <= superior:
        soma = soma + num
        num = num + 1
    print(f"Resultado: {soma}")
"""
"""
num = int(input("Insira o numero que voce quer ver: "))
total = int(input("Total de multiplos que voce quer ver: "))
calc = 1
while calc <= total:
    print(num * calc)
    calc = calc + 1
"""
"""
num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

inferior = num1
superior = num2

if inferior > superior or inferior <= 0 or superior <= 0:
    print("Não é possível calcular.")
else:
    prod = 1
    while inferior <= superior:
        prod = prod * inferior
        inferior = inferior + 1

    print(f"Resultado do produtório: {prod}")
    if prod % 2 == 0:
        print("O resultado é par.")
    else:
        print("O resultado é ímpar.")
"""
"""
num = int(input("Insira número (0 para parar): "))

count = 0
soma = 0

while num != 0:
    count = count + 1
    soma = soma + num
    num = int(input("Insira número (0 para parar): "))

if count > 0:
    media = soma / count
    print(f"Quantidade de números: {count}")
    print(f"Soma: {soma}")
    print(f"Média: {media}")
else:
    print("Nenhum número foi digitado.")
"""
"""
n = int(input("Digite um número inteiro maior que 0: "))

if n <= 0:
    print("O número deve ser maior que 0.")
else:
    resultado = ""
    cont_A = cont_B = cont_C = 0  
    ciclo = ['A', 'B', 'C']
    idx = 0            
    repeticoes = 0    
    i = 0              

    while i < n:
        char = ciclo[idx]
        resultado += char

        if char == 'A':
            cont_A += 1
        elif char == 'B':
            cont_B += 1
        else:
            cont_C += 1

        repeticoes += 1
        if repeticoes == 3:  
            repeticoes = 0
            idx = (idx + 1) % 3

        i += 1

    print(resultado)
    print(f"Quantidade de A: {cont_A}")
    print(f"Quantidade de B: {cont_B}")
    print(f"Quantidade de C: {cont_C}")
    print(f"Retorno do programa (B exibidos): {cont_B}")
"""