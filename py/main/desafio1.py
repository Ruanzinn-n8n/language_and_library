# desafios de fixação do conteúdo dos ultimos 4 dias

# 01
"""print("--------------------------")
print("O numero misterioso...")
print("--------------------------")
print("")
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
par = 0
impar = 0
soma = 0

for i in num:
    num[i] = int(input(f"Digite o {i+1}º número: "))
    soma += num[i]
    if num[i] % 2 == 0:
        par += 1
    else:
        impar += 1

maior = num[0]
menorrr = num[0]

for i in num:
    if i > maior:
        maior = i

    if i < menorrr:
        menorrr = i

print("")
print("---------------------------------------")
print(f"O {maior} é o maior número.")
print(f"O {menorrr} é o menorrr número.")
if par != 1:
    print(f"Tem {par} números pares.")
else:
    print(f"Tem {par} número par")

if impar != 1:
    print(f"Tem {impar} números ímpares.")
else:
    print(f"Tem {impar} número ímpar.")
print("-------------------------------------")
"""
print("")

# 02
"""print("Saque")
print("")
print("Digite o valor que deseja sacar:")
saque = int(input())
print("")
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

if saque < 0:
    print("Você ta lascado KKKKKKKKK")

else:
    while saque >= 100:
        cem += 1
        saque -= 100
    while saque >= 50:
        cinq += 1
        saque -= 50
    while saque >= 20:
        vinte += 1
        saque -= 20
    while saque >= 10:
        dez += 1
        saque -= 10
    while saque >= 5:
        cinco += 1
        saque -= 5
    while saque >= 2:
        dois += 1
        saque -= 2
    while saque >= 1:
        um += 1
        saque -= 1

if cem != 0:
    print(f"Notas de cem: {cem}")
if cinq != 0:
    print(f"Notas de cinquenta: {cinq}")
if vinte != 0:
    print(f"Notas de vinte: {vinte}")
if dez != 0:
    print(f"Notas de dez: {dez}")
if cinco != 0:
    print(f"Notas de cinco: {cinco}")
if dois != 0:
    print(f"Notas de dois: {dois}")
if um != 0:
    print(f"Notas de um: {um}")
"""
print("")

#3

#4

#5

#6
"""print("Notas da turma")
print("-----------------")
alunos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
medias = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Digite a nota dos alunos")

for i in alunos:
    print(f"Aluno {i+1}:")
    nota1 = int(input("--- Nota 1: "))
    nota2 = int(input("--- Nota 2: "))
    medias[i] = (nota1 + nota2)/2
    print(f"Média: {medias[i]}")
    print("")

media_t = (medias[0] + medias[1] + medias[2] + medias[3] + medias[4] + medias[5] + medias[6] + medias[7] + medias[8] + medias[9])/10
maiorr = medias[0]
menorr = medias[0]
apr = 0
rec = 0
rep = 0
for i in medias:
    if maiorr < i:
        maiorr = i
    if menorr > i:
        menorr = i

    if i >= 7:
        apr += 1
    elif i >= 5:
        rec += 1
    else:
        rep += 1

print("")
print("")
print("===== Turma A =====")
print("-------------------")
print(f"Média da turma: {media_t}")
print(f"Maior nota: {maiorr}")
print(f"Menor nota: {menorr}")
print(f"Aprovados: {apr}")
print(f"Recuperação: {rec}")
print(f"Reprovados: {rep}")
"""
print("")

#7
"""print("Maior e Segundo maior")
print("")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Digite 10 números inteiros: ")
for i in nums:
    nums[i] = int(input())

maio = nums[0]
s_maior = 0
for i in nums:
    if i >= maio:
        maio = i
for i in nums:
    if i >= s_maior and i < maio:
        s_maior = i
print("")

print(f" Maior: {maio}")
print(f" Segundo maior: {s_maior}")
"""
print("")

#8
"""print("Sem repetir...")
print("")
num = []
num_s_rep = []

print("Digite 10 números inteiros:")
for i in range(10):
    num.append(int(input("... ")))
for i in num:
    if i not in num_s_rep:
        num_s_rep.append(i)
print("")

print(f"Lista 1: {num}")
print(f"Lista filtrada: {num_s_rep}")
"""
print("")

#9
"""print("Frequência")
print("")
lista = []

print("Digite 10 números")
for i in range(10):
    lista.append(int(input(f"Num {i+1}: ")))

print("")
procurar = int(input("Qual valor deseja encontrar? "))

cont = 0
for i in lista:
    if i == procurar:
        cont += 1

print("")
print(f" O numero {procurar} foi encontrado {cont} vezes.")
"""
print("")

#10
"""print("  Busca")
print("----------")
biblioteca = []

print("Digite 10 números")
for i in range(10):
    biblioteca.append(int(input()))

print("")
print("Qual numero deseja encontrar?")
busca = int(input())
qnt = 0

if busca in biblioteca:
    posicao1 = biblioteca.index(busca)
    posicao2 = len(biblioteca) - 1 - biblioteca[::-1].index(busca)
    for i in biblioteca:
        if i == busca:
            qnt += 1

if qnt > 0:
    print("Existe!!")
    print(f"Quantidade: {qnt}")
    print(f"Primeira posição: {posicao1}")
    print(f"Última posição: {posicao2}")
else:
    print("Não existe!")
"""
print("")

#11
"""print("Votação roubada do Brasil")
print("")
dc = 0
lula = 0
bol = 0
renan = 0
anna = 0
print("---- Digite em quem deseja votar ----")
print("== 13- Lula ladrão    22- Bolsonaro  ==")
print("== 14- Renan santos   11- Anna Júlia ==")

while dc != 1:
    voto = int(input("Digite o número: "))
    print("")
    match voto:
        case 13:
            lula += 1
            print("---- Digite em quem deseja votar ----")
        case 22:
            bol += 1
            print("---- Digite em quem deseja votar ----")
        case 14:
            renan += 1
            print("---- Digite em quem deseja votar ----")
        case 11:
            anna += 1
            print("---- Digite em quem deseja votar ----")
        case 0:
            dc = 1
            print("")
        case _:
            print("voto inválido! tente novamente.")
            print("")
            print("---- Digite em quem deseja votar ----")

print("====== Resultados")
print(f"Lula ladrão: {lula}")
print(f"Bolsonaro: {bol}")
print(f"Renan Santos: {renan}")
print(f"Anna Júlia: {anna}")
"""
print("")

#12
print("--- Caixa Eletrônico ---")
print("------------------------")
saldo = 1000
print("1- Consultar saldo")
print("2- Depositar")
print("3- Sacar")
print("0- Sair")
print("")
dcc = 0

while dcc != 1:
    print("Selecione uma opção:")
    opc = int(input())

    match opc:
        case 1:
            print(f"Saldo: R${saldo}")
        case 2:
            deposito = int(input("Deposite um valor: "))
            if deposito > 0:
                saldo += deposito
                print("Valor depositado com sucesso!")
            else:
                print("Valor inválido!")
        case 3:
            saque = int(input("Digite o valor do saque: "))
            if saque > 0 and saque <= saldo:
                saldo -= saque
                print("Saque feito com sucesso!")
        case 0:
            dcc = 1
        case _:
            print("Opção inválida!")