# Aprendendo sobre estruturas de repetição, como "while" e "for" e a lógica através dela.

# Exercicio 1 - 10xp
print("Exercicio 1 concluido")
print("")
for i in range(1, 11):
    print(i)
print("")

# Exercicio 2 - 10xp
print("Exercicio 2 concluido")
print("")
print("-----------------------------")
n = int(input("Digite um numero inteiro: "))
n += 1
print("-----------------------------")

for i in range(1, n):
    print(i)
print("")

# Exercicio 3 - 15xp
print("Exercicio 3 concluido")
print("")
tab = int(input("Qual tabuada deseja saber? "))
print("------------------------------------")

for i in range(1, 11):
    resul = tab * i
    print(f"{tab}x{i} = {resul}")
print("")

# Exercicio 4 - 20xp
print("Exercicio 4 concluido")
print("")
num = int(input("Digite um número inteiro: "))
print("------------------------------------")
num += 1
soma = 0

for i in range(1, num):
    soma += i
print(f" O resultado é {soma}.")
print("")

# Exercicio 5 - 20xp
print("Exercicio 5 concluido")
print("")
print("------ ACESSAR SISTEMA ------")
senha = ""
cont = 0

while senha != "python27":
    cont += 1
    print("-----------------------------")
    senha = input("--- Digite a senha:  ")
    if senha != "python27":
        print("Senha INCORRETA! tente novamente...")

print("...")
print(f"Senha correta! Você acertou em {cont} tentativas.")
print("Acessando sistema...")
print("")

# Desafio - 40xp
print("Desafio concluido")
print("")
print("========= CONTADOR =========")
print("")
print("---- Digite 10 números:")
cont_p = 0
cont_n = 0
cont_z = 0

for i in range(1, 11):
    num = int(input(f" Número {i}: "))
    if num > 0:
        cont_p += 1
    elif num < 0:
        cont_n += 1
    else:
        cont_z += 1

print("-------------------------")
print(f" Positivos: {cont_p}")
print(f" Negativos: {cont_n}")
print(f" Zeros: {cont_z}")
print("")

# Desafio Bonus - 50xp
print("Desafio bonus")
print("")
print("----- Uma doidera aqui -----")
print("")
qnt = 0
oper = 0
numb = 1
media = 0
teste = 1

while teste != 0:
    print("--- Qual operação deseja fazer?")
    print(" 1 - Adição & Subtração     3 - Divisão")
    print(" 2 - Multiplicação          0 - Sair")
    opc = int(input())

    match opc:
        case 1:
            qnt = 0
            oper = 0
            numb = 1
            media = 0
            while numb != 0:
                numb = int(input("Digite um número: "))
                if numb != 0:
                    qnt += 1
                    oper += numb
                    media = oper / qnt

            print("-------------------------------")
            print(f" Quantidade: {qnt}")
            print(f" Soma: {oper}")
            print(f" Média: {media:.2f}")
            print("")
            
        case 2:
            qnt = 0
            oper = 0
            numb = 1
            oper = 1
            while numb != 0:
                numb = int(input("Digite um número: "))
                if numb != 0:
                    qnt += 1
                    oper *= numb

            print("-------------------------------")
            print(f" Quantidade: {qnt}")
            print(f" Multiplicação: {oper}")
            print("")

        case 3:
            qnt = 0
            oper = 0
            numb = 1
            media = 0
            oper = 1
            while numb != 0:
                numb = int(input("Digite um número: "))
                if numb != 0:
                    qnt += 1
                    oper = numb/oper

            print("-------------------------------")
            print(f" Quantidade: {qnt}")
            print(f" Divisão: {oper}")
            print("")

        case 0:
            teste = 0

        case _:
            print("###### Opção inválida, escolha outra opção:")
print("")

print("Dia 3 finalizado")
print("XP ganho: 165xp")
print("======== Total acumulado: 510XP ==========")