"""
while True:
    try:
        inicio = int(input("Informe o início (inteiro positivo): "))
        fim = int(input("Informe o fim (inteiro positivo): "))
        if inicio > 0 and fim > 0:
            break
        else:
            print("Ambos devem ser inteiros positivos. Tente novamente.\n")
    except ValueError:
        print("Entrada inválida. Digite apenas inteiros.\n")

if inicio > fim:
    inicio, fim = fim, inicio

for n in range(inicio, fim + 1):
    print(f"Tabuada do {n}:")
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1
    print()
"""
"""
while True:
    try:
        qt = int(input("Quantidade de números a ler (inteiro positivo): "))
        if qt > 0:
            break
        else:
            print("A quantidade deve ser > 0.\n")
    except ValueError:
        print("Entrada inválida. Digite um inteiro.\n")

soma_fatoriais = 0

for k in range(1, qt + 1):
    while True:
        try:
            n = int(input(f"Informe o {k}º número (inteiro >= 0): "))
            if n >= 0:
                break
            else:
                print("O número deve ser >= 0.\n")
        except ValueError:
            print("Entrada inválida. Digite um inteiro.\n")

    f = 1
    i = 2
    while i <= n:
        f *= i
        i += 1

    soma_fatoriais += f

print(f"Somatório dos fatoriais = {soma_fatoriais}")
"""
"""
while True:
    try:
        linhas = int(input("Quantidade de linhas (> 0): "))
        if linhas > 0:
            break
        else:
            print("A quantidade deve ser > 0.\n")
    except ValueError:
        print("Entrada inválida. Digite um inteiro.\n")

for i in range(1, linhas + 1):
    linha = ""
    j = 1
    while j <= i:
        if j > 1:
            linha += " "
        linha += "*"
        j += 1
    print(linha)
"""
"""
while True:
    try:
        linhas = int(input("Quantidade de linhas (> 0): "))
        if linhas > 0:
            break
        else:
            print("A quantidade deve ser > 0.\n")
    except ValueError:
        print("Entrada inválida. Digite um inteiro.\n")

i = 1
while i <= linhas:
    linha = ""
    j = 1
    while j <= i:
        if j > 1:
            linha += " "
        linha += "*"
        j += 1
    print(linha)
    i += 1

# parte decrescente
i = linhas - 1
while i >= 1:
    linha = ""
    j = 1
    while j <= i:
        if j > 1:
            linha += " "
        linha += "*"
        j += 1
    print(linha)
    i -= 1
"""