#vou usar os comentários apenas para voce indentificar qual exercicio é qual, pode ignorar eles.

# Exercicio 1
n = int(input())
numeros = []
for i in range(n):
    numeros.append(int(input()))
numeros.sort()
print(f"Maior: {numeros[n-1]}")
print(f"Menor: {numeros[0]}")
print(numeros)

# Exercicio 2
n = int(input())
nums = list(map(int, input().split()))
dif = set(nums)
print(len(dif))

# Exercicio 3
numeros = list(map(int, input().split()))
maior = numeros[0]
i_maior = 0
for i, numero in enumerate(numeros):
    if numero > maior:
        maior = numero
        i_maior = i
print(i_maior, maior)

# Exercicio 4
nomes = list(input().split())
notas = list(map(int, input().split()))
for nome, nota in zip(nomes, notas):
    print(nome, nota)

# Exercicio 5
def freq(n):
    uni = {}
    for i in n:
        if i in uni:
            uni[i] += 1
        else:
            uni[i] = 1
    return uni

nums = list(map(int, input().split()))
resultado = freq(nums)
for i in resultado:
    print(f"{i}: {resultado[i]}")

# Exercicio 6
n = list(map(int, input().split()))
unicos = set(n)
rev = []
for i in unicos:
    rev.append(i)
rev.sort(reverse=True)
print(rev[1])

# Exercicio 7
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for i in list2:
    list1.append(i)
limpa = set(list1)
list3 = []
for i in limpa:
    list3.append(i)
list3.sort()
print(list3)