import time

def ler_voto():
    while True:
        opcs = ["0","1","2","3","4","5","6","urna"]
        opc = input("Digite o número do seu voto:\n").lower()
        if opc not in opcs:
            print("Digite um valor entre 0 e 6! ou 'Urna' para ver as opções")
        else:
            break
    return opc

candidatos = {
    "Paulo Matagal": 0,
    "Finácio Polvo": 0,
    "Gusto Cuty Cuty": 0,
    "Márcio Malonaro": 0,
    "Nulo": 0,
    "Branco": 0
    }
def cont_voto(opc):
    ver = 0
    sair = 0
    match opc:
        case "1":
            print("Votando em Paulo Matagal...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["Paulo Matagal"] += 1
        case "2":
            print("Votando em Finácio Polvo...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["Finácio Polvo"] += 1
        case "3":
            print("Votando em Gusto Cuty Cuty...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["Gusto Cuty Cuty"] += 1
        case "4":
            print("Votando em Márcio Malonaro...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["Márcio Malonaro"] += 1
        case "5":
            while True:
                print("Tem certeza que deseja ANULAR seu voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["Nulo"] += 1
        case "6":
            while True:
                print("Tem certeza que deseja votar em BRANCO? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["Branco"] += 1
        case "0":
            sair = 1
        case "urna":
            ver = 1
    return candidatos, sair, ver

def calculo(dic):
    tot = 0
    #total de x em dic = dic[x]
    for i in dic:
        tot += dic[i]
    try:
        porc_nulo = (dic["Nulo"] / tot) * 100
    except ZeroDivisionError:
        porc_nulo = 0
    try:
        porc_branco = (dic["Branco"] / tot) * 100
    except ZeroDivisionError:
        porc_branco = 0
    venc = 0
    venc_name = 0
    for i, j in dic.items():
        if j > venc and "Nulo" != i != "Branco":
            venc = j
            venc_name = i
        elif j == venc and "Nulo" != i != "Branco":
            venc_name = f"Empate!"
    return tot, porc_nulo, porc_branco, venc_name

def urna():
    dc = 0
    while True:
        if dc == 0:
            print("+=======================+")
            print("|   - Urna de votação   |")
            print("|=======================|")
            print("|  - Opções de voto:    |")
            print("| - - - - - - - - - - - |")
            print("| 1- Paulo Matagal      |")
            print("| 2- Finácio Polvo     |")
            print("| 3- Gusto Cuty Cuty    |")
            print("| 4- Márcio Malonaro    |")
            print("| 5- Voto Nulo ###      |")
            print("| 6- Voto em Branco ### |")
            print("| 0- Sair da votação    |")
            print("|                       |")
            print("|=======================|\n")
            print("### Para ver as opções novamente escreva 'Urna'")
            dc = 1
        voto = ler_voto()
        resul, sair, urna = cont_voto(voto)
        if urna == 1:
            dc = 0
        if sair == 1:
            total, nulo, branco, vencedor = calculo(resul)
            print("Votação encerrada! Aguarde o resultado...")
            time.sleep(1)
            print("#############################")
            print("##        Resultado        ##")
            print("#############################")
            print(f"## Paulo Matagal: {resul["Paulo Matagal"]}")
            print(f"## Finácio Polvo: {resul["Finácio Polvo"]}")
            print(f"## Gusto Cuty Cuty: {resul["Gusto Cuty Cuty"]}")
            print(f"## Márcio Malonaro: {resul["Márcio Malonaro"]}")
            print(f"## Votos Nulos: {resul["Nulo"]}")
            print(f"## Votos em Branco: {resul["Branco"]}")
            print(f"## % de votos nulos: {nulo:.2f}%")
            print(f"## % de votos em Branco: {branco:.2f}%")
            print(f"## Total: {total}")
            print(f"##### Candidato Vencedor: {vencedor}")
            break
        else:
            print("\nVoto concluído!")
            print("...\n")
            time.sleep(0.5)
            print("\nPróximo a votar...")

print("Sistema de Votação iniciado!")
print("Aguarde...")
time.sleep(1)
urna()