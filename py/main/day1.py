# - Aprendendo a usar o input, f-strings e fixação do :.2f

# Exercicio 1 - 10xp
print("Exercicio 1 concluido")
nome = input("Qual seu nome? ")
idade = int(input(f"Olá {nome}, quantos anos você tem? "))
print("")
print("Informação guardada com sucesso!")
print(f"O usuário {nome} tem {idade} anos...")
print("")

# Exercicio 2 - 10xp
print("Exercicio 2 concluido")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print("")

print(f"Adição: {num1} + {num2} = {num1+num2}")
print(f"Subtração: {num1} - {num2} = {num1-num2}")
print(f"Multiplicação: {num1} x {num2} = {num1*num2}")
print(f"Divisão: {num1}/{num2} = {num1/num2:.2f}")
print("")

# Exercicio 3 - 10xp
print("Exercicio 3 concluido")
print("Veja quanto gastou...")
prod = input("Oque você comprou? ")
qnt = int(input(f"Ótimo! e qual a quantidade de {prod +"s"}? "))
preco = float(input(f"Por ultimo, qual preço do item? "))
print("")
print(f"Você gastou exatamente {preco*qnt} na compra de {qnt} {prod +"s"}!")
print("")

# Exercicio 4 - 20xp
print("Exercicio 4 concluido")
print("Veja seu boletim e média bimestral!")
print("")
nome = input("Qual seu nome? ")
nota_pyt = float(input("Qual sua nota em Python? "))
nota_java = float(input("Qual sua nota em Java? "))
nota_css = float(input("Qual sua nota em CSS? "))
media = (nota_pyt + nota_java + nota_css)/3
print("")
print("===============")
print("    BOLETIM    ")
print("===============")
print(f"Aluno: {nome}")
print("---------------")
print(f"Python --- {nota_pyt:.2f}")
print(f"Java ----- {nota_java:.2f}")
print(f"CSS ------ {nota_css:.2f}")
print("---------------")
print(f"Média ---- {media:.2f}")
print("")

# Exercicio 5 - 20xp
print("Exercicio 5 concluido")
print("Seu salário, Seu sustento...")
print("")
nome = input("Primeiro, Qual seu nome? ")
emprego = input(f"Ótimo {nome}, e sua profissão? ")
sal_mensal = float(input("Quanto você recebe por mês? "))
sal_anual = sal_mensal * 12
print("")
print(f"Ok {nome},")
print(f"no seu trabalho como {emprego} você recebe:")
print(f"por mês: {sal_mensal}")
print(f"por ano: {sal_anual:.2f}")
print("")

# BONUS - 40XP
print("Exercicio Bonus Concluido")
print("")
valor = int(input("Digite os segundos: "))
print("")

hora = valor // 3600
rest = valor % 3600
minutos = rest // 60
seg = rest % 60

if hora == 1:
    hr = "horas"
else:
    hr = "hora"

print("=================================")
print("       CONVERSOR DE TEMPO        ")
print("=================================")
print(f"Valor Recebido: -------- {valor}")
print("")
print(f"{hora} {hr}, {minutos} minutos e {seg} segundos")
print("")
print("=================================")
print("")

print("-------------------------------------------")
print("Dia 1 finalizado")
print("XP ganho: 110xp")
print("======== Total acumulado: 200XP ==========")