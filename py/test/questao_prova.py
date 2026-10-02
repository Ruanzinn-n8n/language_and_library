#  Questão - o código precisa receber N numeros. Dos N numeros, o código deve fazer
# a maior pontuação. o "jogo" funciona assim: A pontuação começa em 0 e haverá N
# numeros, ao remover um número P, o valor de P é somado a pontuação porém dos números
# é removido P+1 e P-1 que não são somados a pontuação. Após isso ele remove outro
# número, e se repete até acabar todos os numeros.
#   Por exemplo:
# números = {1, 2, 3, 4, 5}
# "remove o 1" pontuação = 1 e sai da lista o 1 e o 2. sobra: {3, 4, 5}
# "remove o 3" pontuação = 4 e sai da lista o 3 e o 4. sobra: {5}
# "remove o 5" pontuação = 9.
#   Outro exemplo:
# números = {3, 3, 5, 4, 2}
# "remove o 3" pontuação = 3 e sai da lista o 3, o 4 e o 2. sobra: {3, 5}
# "remove o 3" pontuação = 6 e sai da lista apenas o 3. sobra: {5}
# "remove o 5" pontuação = 11.
"""
def pontuacao(lista):
    soma = 0
    while len(lista) != 0:
        for i in lista:
            maior = i+1
            menor = i-1
            if maior not in lista:
                soma += i
                lista.remove(i)
                if menor in lista:
                 lista.remove(menor)
    return soma

nums = list(map(int, input().split(",")))
pontos = pontuacao(nums)
print(pontos)
"""

#    Questão 10 - Sudoku
# A questão pede que o programa receba uma entrada de numeros de um sudoku em que
# o numero 0 representa um espaço vazio. o programa deve retornar o sudoku resolvido
# e preenchido de acordo as regras do sudoku clássico.

def org_sudoku(input):
    list_inp = list(map(int, input.split(",")))
    sudoku = []
    tam = len(list_inp)
    for i in range(0, tam, 9):
        linha_subs = []
        for j in range(9):
            n = i+j
            linha_subs.append(list_inp[n])
        sudoku.append(linha_subs.copy())
    return sudoku

def preencher(sudoku_org):
    sudoku = []
    tam = len(sudoku_org)
    for linha in range(tam):
        new_line = []
        for coluna in range(tam):
            test = sudoku_org[linha][coluna]
            if test != 0:
                new_line.append(test)
            else:
                for i in range(tam):
                    if i+1 not in sudoku_org[linha]:
                        for j in range(tam):
                            if i+1 != sudoku_org[j][coluna]:
                                test = j
                new_line.append(test)
        sudoku.append(new_line)
    return sudoku




entrada = "5,3,0,0,7,0,0,0,0,6,0,0,1,9,5,0,0,0,0,9,8,0,0,0,0,6,0,8,0,0,0,6,0,0,0,3,4,0,0,8,0,3,0,0,1,7,0,0,0,2,0,0,0,6,0,6,0,0,0,0,2,8,0,0,0,0,4,1,9,0,0,5,0,0,0,0,8,0,0,7,9"

teste = org_sudoku(entrada)
for i in teste:
    print(*i)