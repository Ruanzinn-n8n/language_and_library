print("Questão 1 - Strings - concluida")
print("")

def string_unica(texto):
    palavra = texto
    for i in palavra:
        cont = 0
        for f in palavra:
            if i == f:
                cont += 1
            if cont > 1:
                return False
    return True

receba = input("Digite uma palavra:  ")
resultado = string_unica(receba)
print("")
print(resultado)
print("")

print("Questão 2 - Frequência")
print("")

def frequencia(numeros):
    for i in numeros:
        cont = 0
        for f in numeros:
            if i == f:
                cont += 1
        print(f"O número {i} apareceu {cont} vezes!")

# não consegui fazer com que falasse apenas 1 vez para cada número.

lista = []
print("Digite 8 números;")
for i in range(8):
    lista.append(int(input(f"N°{i+1}: ")))

frequencia(lista)
print("")

print("Questão 3 - Segundo Maior")
print("")

def segundo_maior(numeros):
    maior = numeros[0]
    s_maior = numeros[0]
    for i in numeros:
        if i > maior:
            maior = i
    for i in numeros:
        if i > s_maior and i < maior:
            s_maior = i
    return s_maior

lista = []
print("Digite 6 números;")
for i in range(6):
    lista.append(int(input(f"N°{i+1}: ")))
print("")
print(segundo_maior(lista))
print("")

print("Questão 4 - Anagrama - concluido")
print("")

def anagrama(text1, text2):
    tamanho1 = len(text1) -1
    tamanho2  = len(text2) -1
    if tamanho1 == tamanho2:
        for i in text1:
            cont = 0
            for j in text2:
                if i == j:
                    cont += 1
            if cont > 1 or cont < 1:
                return False
    else:
        return False
    return True

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

resultado = anagrama(palavra1, palavra2)
print(resultado)
print("")

print("Questão 5 - Binário")
#não consegui fazer
print("")

print("Questão 6 - Dicionário")
print("")

def dicionario(valores):
    cont = 0
    soma = 0
    maior = 0
    for i in valores:
        soma += valores[i]
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] >= 7:
            cont += 1
    media = soma/len(valores)
    menor = maior
    for i in valores:
        if valores[i] < menor:
            menor = valores[i]
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Média da turma: {media}")
    print(f"Alunos aprovados: {cont}")

alunos = {
    "Ruan": 8.5,
    "Lucas": 6.0,
    "Higor": 9.2,
    "Samira": 7.8
}

dicionario(alunos)
#não deu certo n sei porque, mas acredito que seja uma coisa simples, porém acho que já tentei tudo que sei.
print("")

#da questão 7 e a 8 não sei como fazer também

print("Questão 9")
""" A 9 não entendi se é para criar um programa que faz isso ou se é para
 apenas responder, acho que é para responder então: Sim, a expressão está com os parenteses corretos!"""
print("")

# A questão 10 também não sei.

print("Questão 11 - debugging")
# 1- O erro está no laço "FOR".
# 2- Está errado porque está usando o |range(len(numeros))| e graças a isso o "i" é o indice e não o valor. além disso também está errado na soma em que está apenas atribuindo o 1 a variável soma.
# 3- Corrigindo fica:
numeros = [10, 20, 30, 40]

soma = 0
for i in numeros:
    soma += i

media = soma / len(numeros)
print(media)