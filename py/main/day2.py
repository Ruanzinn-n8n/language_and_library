# aprendendo mais sobre if, elif e else. suas condições e operadores.

# Exercicio 1 - 10xp
print("Exercicio 1 concluido")
print("")
idad = int(input("Quantos anos você tem? "))

if idad >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
print("")

# Exercicio 2 - 10xp
print("Exercicio 2 concluido")
print("")
num = int(input("Digite um numero inteiro: "))

if num > 0:
    print(f"{num} é um inteiro POSITIVO")
elif num < 0:
    print(f"{num} é um inteiro NEGATIVO")
else:
    print("ZERO")
print("")

# Exercicio 3 - 15xp
print("Exercicio 3 concluido")
print("")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

print("")
if media >= 7:
    print(f"Sua média é {media:.2f}, você foi APROVADO")
elif media >= 5:
    print(f"Sua média é {media:.2f}, você está de RECUPERAÇÃO")
else:
    print(f"Sua média é {media:.2f}, voce foi REPROVADO")
print("")

# Exercicio 4 - 20xp
print("Exercicio 4 concluido")
print("")
print("---- Classificação de idade ----")
print("")
idade = int(input("Qual sua idade? "))
print("")

if idade <= 12:
    print(f"Você tem {idade} anos, é uma criança.")
elif idade <= 17:
    print(f"Você tem {idade} anos, é um adolescente.")
elif idade <= 59:
    print(f"Você tem {idade} anos, é um adulto.")
else:
    print(f"Você tem {idade} anos, é idoso.")
print("")

# Exercicio 5 - 20xp
print("Exercicio 5 concluido")
print("")
print("---- Quer dirigir? ----")
print("")
idades = int(input("Quantos anos você tem? "))
cnh = input("Possui CNH? ")
sim = "Sim", "sim", "s", "S", "yes", "Yes", "SIM"
nao = "Nao", "Não", "nao", "não", "n", "N", "no", "NO"

if idades >= 18 and cnh in sim:
    print(f"Você tem {idades} anos e possui a CNH.")
    print("=== Pode dirigir ===")
elif idades >= 18 and cnh in nao:
    print(f"Você tem {idades} anos mas não possui a CNH.")
    print("=== Não pode dirigir ===")
else:
    print("Você é menor de idade, logo não tem permissão para dirigir!")
print("")

# Desafio - 40XP
print("Desafio concluido")
print("")
print("--- Maior e Menor ---")
print("")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
print("")

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print("-----------------------------")
print(f" Primeiro numero: {num1}")
print(f" Segundo numero: {num2}")
print(f" Terceiro numero: {num3}")
print("")
print(f" Maior: {maior}")
print(f" Menor: {menor}")
print("")

# Desafio extra - 30xp
print("Extra")
print("")
print("---- ENTRAR ----")
print("")
senha_d = input("Digite a senha de 8 digitos: ")
senha_n = input("Digite a senha numérica: ")
d_ok = "python27"
n_ok = "080826"

if senha_d == d_ok and senha_n == n_ok:
    print("Acesso Permitido...")
else:
    print("!!!! Acesso NEGADO !!!!")
print("")

print("Dia 2 finalizado")
print("XP ganho: 145xp")
print("======== Total acumulado: 345XP ==========")