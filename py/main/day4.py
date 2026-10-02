# aprendendo sobre listas

# Exercicio 1 - 10xp
print("Exercicio 1 concluido")
print("")
numeros = [1, 6, 4, 3, 6]

for numero in numeros:
    print(numero)
print("//")

# Exercicio 2 - 10xp
print("Exercicio 2 concluido")
print("")
nomes = ["Ruan", "Samira", "Lucas", "Higor", "Costelinha"]
dc = 1
while dc != 0:
    print("Digite um nome:")
    nome = input()
    print("")
    if nome in nomes:
        print(f"{nome} está na lista!")
        print("")
    elif nome == "0":
        dc = 0
    else:
        print(f"{nome} não está na lista!")
        print("")
print("//")

# Exercicio 3 - 15xp
print("Exercicio 3 concluido")
print("")
numeross = [2, 3, 6, 5, 8, 18, -10, 0]

for numeroo in numeross:
    if (numeroo % 2) == 0:
        print(numeroo) 
print("//")

# Exercicio 4 - 20xp
print("Exercicio 4 concluido")
print("")
nums = [-2, 5, 0, 7, -1, -7, 0, 4, 3, 10]
p = 0
n = 0
z = 0

for i in nums:
    if i > 0:
        p += 1
    elif i < 0:
        n += 1
    else:
        z += 1
print(f"- Positivos: {p}")
print(f"- Negativos: {n}")
print(f"- Zeros: {z}")
print("//")

# Exercicio 5 - 20xp
print("Exercicio 5 concluido")
print("")
num = [1712, 1709, 2008, 1986, 2015, 2023]
dp = 1

while dp != 0:
    print("Digite um número: ")
    opc = int(input())
    print("")
    if opc != 0:
        for i in range(len(num)):
            if num[i] == opc:
                resul = (f"Número {num[i]} encontrado na posição {(i)+1}!")
                break
            else:
                resul = ("Número não encontrado...")
        print(resul)
        print("")
    else:
        dp = 0
print("//")

# Bonus - 50xp
print("Exercicio BONUS concluido")
print("")
print("Digite um nome:")
name = input()
letras = len(name)
cont = 0
a = ("a", "A")
print("")

for na in name:
    if na in a:
        cont += 1

print("----------------")
print(f" Letras: {letras}")
print(f" Primeira letra: {name[0]}")
print(f" Ultima letra: {name[letras-1]}")
print(f" Quantidade de A: {cont}")
print("")

print("Dia 4 finalizado")
print("XP ganho: 165xp")
print("======== Total acumulado: 675XP ==========")
