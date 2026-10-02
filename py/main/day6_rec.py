print("Rec 1 - concluida")
print("")

def num_bin(num):
    bin = []
    while num != 0:
        sobra = num % 2
        bin.append(sobra)
        num = num // 2
    return bin
def inverter(lista):
    bin = []
    tam = len(lista) -1
    for i in range(len(lista)):
        n_oposto = tam -i
        bin.append(lista[n_oposto])
    return bin

n = 0
while n <= 0:
    n = int(input("Digite o número para conversão: "))
    if n <= 0:
        print("Número inválido, digite um número maior que 0!")

num = num_bin(n)
n_binario = inverter(num)
str_bin = []
for i in n_binario:
    n_bin = str(i)
    str_bin.append(n_bin)
j_bin = "".join(str_bin)
print(j_bin)


print("Rec 2 - corrigida")
print("")

def troca(frase):
    inv = []
    if len(frase) % 2 == 0:
        for i in range(0, len(frase), 2):
            inv.append(frase[i+1])
            inv.append(frase[i])
    else:
        for i in range(0, len(frase), 2):
            if i == len(frase)-1:
                inv.append(frase[i])
            else:
                inv.append(frase[i+1])
                inv.append(frase[i])
    return(inv)

print("Digite uma frase:")
text = list(input().split())
frase = troca(text)
teste = " ".join(frase)
print(teste)


print("Rec 3 - concluido")
print("")

def frequencia(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print("Digite os números:")
receba = list(map(int, input().split()))
teste = frequencia(receba)
print(teste)


print("Rec 4 - concluida")
print("")

def juntar_etc(nums1, nums2):
    list1 = list(map(int, nums1.split()))
    list2 = list(map(int, nums2.split()))
    inv = []
    soma = 0
    for i in list2:
        list1.append(i)
    tam = len(list1) -1
    for i in range(len(list1)):
        n_op = tam -i
        inv.append(list1[n_op])
    for i in inv:
        soma += i
    return list1, inv, soma

print("Digite a lista 1:")
l1 = input()
print("")
print("Digite a lista 2:")
l2 = input()

completa, contraria, total = juntar_etc(l1, l2)
print("")
print(f"Lista completa: {completa}")
print(f"Lista invertida: {contraria}")
print(f"Soma: {total}")

print("Rec 5 -")
print("")

def media():
    notas = {}
    soma_p = 0
    soma_n = 0
    for i in range(3):
        notas[f"Nota {i+1}"] = 0
        print(f"Digite e nota {i+1} e seu peso:")
        nota_peso = list(map(int, input().split()))
        notas[f"Nota {i+1}"] = nota_peso[0]*nota_peso[1]
        soma_n += (nota_peso[0]*nota_peso[1])
        soma_p += nota_peso[1]
    media_p = soma_n/soma_p
    return notas, media_p

notas, ponderada = media()

print("")
for i in notas:
    print(f"{i}: {notas[i]}")
print(f"Média = {ponderada}")
