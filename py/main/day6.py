print("Exercicio 1 - concluido")
print("")
a, b = map(int, input("Digite 2 valores: ").split())
print(a + b)


print("Exercicio 2 - concluido")
print("")
a, b, c = map(int, input("Digite 3 valores: ").split())
media = (a+b+c)/3
print(f"{media:.2f}")

print("Exercicio 3 - concluido")
print("")
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for i in lista:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

n = int(input("Digite uma quantidade N: "))
numeros = list(map(int, input("Digite N numeros: ").split()))

maior_menor(numeros)

print("Exercicio 4 - concluido")
print("")

def inverter(lista):
    lista_inv = []
    tam = len(lista) -1
    for i in range(len(lista)):
        n_oposto = tam -i
        lista_inv.append(lista[n_oposto])
    print(lista_inv)

numeros = list(map(int, input("Digite os numeros: ").split()))
inverter(numeros)

print("Exercicio 5 - concluido")
print("")

def eh_par(lista):
    cont = 0
    for i in lista:
        if i % 2 == 0:
            cont += 1
    print(cont)

n = int(input("Digite uma quantidade N: "))
print(f"Digite {n} números:")
numeros = list(map(int, input().split()))

eh_par(numeros)

print("Exercicio 6 - concluido")
print("")

def pos_neg(lista):
    p = 0
    n = 0
    z = 0
    soma = 0
    for i in lista:
        if i > 0:
            soma += i
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    print(f"Positivos: {p}")
    print(f"Soma: {soma}")
    print(f"Negativos: {n}")
    print(f"Zeros: {z}")
#tratei o 0
n = int(input("Digite uma quantidade N: "))
print(f"Digite {n} números:")
numeros = list(map(int, input().split()))

pos_neg(numeros)

print("Exercicio 7 -")
print("")
# Eu não fiz nenhum exercicio anterior, quando disse pra refazer as questões com base no que meu amigo falou você considerou que eu havia feito as questões, mas como era pra refazer então n fiz. após corrigir esse me passe outros exercicios ensinando oque vc tinha dito antes e ai depois a gnt avança.

print("Exercicio 8 - concluido")
print("")

def ingres(n):
    ingles = [
        "Zero", "One", "Two", "Three", "Four", 
        "Five", "Six", "Seven", "Eight", "Nine"
        ]
    #não tenho certeza se a escrita tá certa kkkkk
    print(ingles[n])

print("Digite um número de 0 a 9:")
dc = 0
while dc == 0:
    num = int(input())
    if num > 9 or num < 0:
        print("Número inválido! Digite outro:")
    else:
        dc = 1
ingres(num)

print("Exercicio 9 -")
print("")

# N faço a menor ideia pq n sei mt sobre numeros binários kkkk me ensine junto com as outras coisas e já coloque nos próximos exercicios.

print("Exercicio 10 -")
print("")
# Infelismente também não sei kkk mas acredito que vai usar aquele metodo ::: que você comentou antes, porém como n li os ultimos exercicios também n sei, me ensina sobre e também põe no próximo