"""
def eh_primo(n: int) -> bool:
    if n is None:
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    return linhas, colunas
"""
"""
def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        for valor in linha:
            soma += valor
    return soma
"""
"""
def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(x) for x in linha))
"""
"""
def maior_texto_matriz(matriz):
    maior = ""
    for linha in matriz:
        for texto in linha:
            if len(texto) > len(maior):
                maior = texto
    return maior
"""
"""
def menor_elemento_e_posicao(matriz):
    menor = matriz[0][0]
    lin_menor = 0
    col_menor = 0
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor < menor:
                menor = valor
                lin_menor = i
                col_menor = j
    return [menor, lin_menor, col_menor]
"""
"""
def conta_primos_matriz(matriz):
    cont = 0
    for linha in matriz:
        for valor in linha:
            if eh_primo(valor):
                cont += 1
    return cont
"""
"""
def contem_numero(matriz, numero):
    for linha in matriz:
        if numero in linha:
            return True
    return False
"""
"""
def eh_quadrada(matriz):
    linhas, colunas = dimensoes(matriz)
    return linhas == colunas
"""
"""
def soma_colunas_matriz_quadrada(matriz):
    if not eh_quadrada(matriz):
        return None
    n, _ = dimensoes(matriz)
    somas = [0] * n
    for i in range(n):
        for j in range(n):
            somas[j] += matriz[i][j]
    return somas
"""
"""
def linhas_colunas_nulas(matriz):
    linhas, colunas = dimensoes(matriz)
    linhas_vazias = set()
    colunas_vazias = set()
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == '':
                linhas_vazias.add(i)
                colunas_vazias.add(j)
    return linhas_vazias, colunas_vazias
"""
"""
def linhas_colunas_so_negativos(matriz):
    linhas, colunas = dimensoes(matriz)

    linhas_so_neg = set()
    for i in range(linhas):
        if all(matriz[i][j] < 0 for j in range(colunas)):
            linhas_so_neg.add(i)

    colunas_so_neg = set()
    for j in range(colunas):
        if all(matriz[i][j] < 0 for i in range(linhas)):
            colunas_so_neg.add(j)

    return linhas_so_neg, colunas_so_neg
"""
"""
def eh_simetrica(matriz):
    if not eh_quadrada(matriz):
        return False
    n, _ = dimensoes(matriz)
    for i in range(n):
        for j in range(i + 1, n):  
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
"""
"""
def elemento_minmax(matriz):
    menor = matriz[0][0]
    lin_menor = 0
    col_menor = 0
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor < menor:
                menor = valor
                lin_menor = i
                col_menor = j  # não é tão usado, mas guardamos

    linha_escolhida = matriz[lin_menor]
    max_linha = linha_escolhida[0]
    col_max = 0
    for j, valor in enumerate(linha_escolhida):
        if valor > max_linha:
            max_linha = valor
            col_max = j

    return [lin_menor, col_max, max_linha]
"""
"""
def pontos_de_sela(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    resultados = []

    for i in range(linhas):
        menor_linha = min(matriz[i])
        for j in range(colunas):
            if matriz[i][j] == menor_linha:
                valor = matriz[i][j]
                maior_coluna = True
                for k in range(linhas):
                    if matriz[k][j] > valor:
                        maior_coluna = False
                        break
                if maior_coluna:
                    resultados.append((i, j, valor))
    return resultados
"""
"""
def elementos_unicos(matriz):
    unicos = []
    for linha in matriz:
        for valor in linha:
            if valor not in unicos:
                unicos.append(valor)
    return unicos
"""
"""
def contagem_elementos(matriz):
    cont = {}
    for linha in matriz:
        for valor in linha:
            if valor in cont:
                cont[valor] += 1
            else:
                cont[valor] = 1
    return cont
"""