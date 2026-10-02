# Aprendendo funções | def nome_funcao():

# Exercicio 1 - 10xp
print("Exercicio 1 concluido")
print("")
def saudacao(nome):
    print(f"Olá {nome}, saudações!")

pessoa = input("Digite seu nome: ")
i = pessoa
saudacao(i)
print("")

# Exercicio 2 - 10xp
print("Exercicio 2 concluido")
print("")
def soma(a, b):
    return a + b

resultado = soma(1000, -7)
print(resultado)
print("")

# Exercicio 3 - 15xp
print("Exercicio 3 concluido")
print("")
def eh_par(numero):
    if (numero % 2) == 0:
        return True
    else:
        return False

valor = int(input("Digite um número: "))
resultado = eh_par(valor)
print(resultado)
print("")

# Exercicio 4 - 20xp
print("Exercicio 4 concluido")
print("")
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3)/3
def situacao(media):
    if media >= 7:
        print("Aprovado!")
    elif media >= 5:
        print("Recuperação!")
    else:
        print("Reprovado!")

nota = calcular_media(7, 10, 9)
situacao(nota)
print("")

# Exercicio 5 - 20xp
print("Exercicio 5 concluido")
print("")
print("Positivos e negativos")
print("")

def analisar_lista(numeros):
    quanto = int(input("Quantos números deseja contar: "))
    for i in range(quanto):
        numeros.append(int(input(f"Número {i+1}:  ")))
    p = 0
    n = 0
    z = 0
    for i in numeros:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    print(f"Postivos: {p}")
    print(f"Negativos: {n}")
    print(f"Zeros: {z}")
lista = []

analisar_lista(lista)
print("")

# Exercicio 6 - 25xp
print("Exercicio 6 concluido")
print("")
def maior_numero():
    lista = []
    maior = 0
    print("Digite um número:")
    for i in range(5):
        lista.append(int(input()))
    for i in lista:
        if i > maior:
            maior = i
    print(f"O maior é: {maior}")
def menor_numero():
    lista = []
    print("Digite um número:")
    for i in range(5):
        lista.append(int(input()))
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    print(f"O menor é: {menor}")

maior_numero()
menor_numero()
print("")

# Exercicio 7 - 25xp
print("Exercicio 7 concluido")
print("")
def contar_letra(texto, letra):
    cont = 0
    palavra = texto
    for i in palavra:
        if i == letra:
            cont += 1
    print(f"Na palavra {texto} tem {cont} letras {letra}!")

contar_letra("banana", "a")
print("")

# Exercicio 8 - 30xp
print("Exercicio 8 concluido")
print("")
print("É um palindromo?")

def eh_palindromo(texto):
    cont = 0
    palavra = texto
    tamanho = len(palavra) - 1
    for i in range(len(palavra)):
        n_oposto = tamanho - i
        letra = palavra[i]
        l_oposta = palavra[n_oposto]
        if letra == l_oposta:
            cont += 1
        
    if cont == len(palavra):
        return True
    else:
        return False

palavra = input("Digite uma palavra:  ")

resultado = eh_palindromo(palavra)
print(resultado)
print("")