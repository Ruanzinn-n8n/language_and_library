# Aprendendo sobre matrizes

print("Exercicio 1, 2, 3, 4, 5, 6 - concluido")
#1
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for i in range(len(matriz)):
    tam = len(matriz[i])
    print(matriz[i][-i])

#2
matriz2 = matriz
matriz2[1][1] = 500
print(matriz2)

#3
print(matriz[1][1])
print(matriz[1])
for i in matriz:
    for j in i:
        print(j)

#4, 5
soma = 0
par = 0
for i in matriz:
    for j in i:
        soma += j
        if j % 2 == 0:
            par += 1
print(soma)
print(par)

#6
maior = matriz[0][0]
menor = matriz[0][0]
for i in matriz:
    for j in i:
        if j > maior:
            maior = j
    for j in i:
        if j < menor:
            menor = j
print(menor)
print(maior)

#7, 8
soma_p = 0
soma_s = 0
for i in range(len(matriz)):
    print(matriz[i][i])
    soma_p += matriz[i][i]
print(soma_p)
for i in range(len(matriz)):
    tam7 = len(matriz[i])
    n = matriz[i][tam7 -1 -i]
    soma_s += n
    print(n)
print(soma_s)

#9, 10
n = int(input())
dc = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == n:
            print(f"Número encontrado na posição: {i}, {j}")
    if n not in matriz[i]:
        dc += 1
if dc == len(matriz):
    print("Não encontrado!!!!!!!")


print("Desafio")
matrizz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_inv = []
tam_m = len(matrizz) -1
for i in range(len(matrizz)):
    matriz_inv.append(matrizz[tam_m -i].copy())
for i in matriz_inv:
    i.reverse()

for i in matrizz:
    print(*i)
print("")
for i in matriz_inv:
    print(*i)