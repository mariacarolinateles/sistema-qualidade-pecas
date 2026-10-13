pecas_aprovadas = []
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []

def id_ja_cadastrado(id_peca):
    for peca in pecas_aprovadas:
        if peca["id"] == id_peca:
            return True

    for peca in pecas_reprovadas:
        if peca["id"] == id_peca:
            return True

    return False

def listar_pecas():
    print()
    print("========================================")
    print("          LISTA DE PEÇAS")
    print("========================================")

    print()
    print("PEÇAS APROVADAS:")

    if len(pecas_aprovadas) == 0:
        print("Nenhuma peça aprovada.")
    else:
        for peca in pecas_aprovadas:
            print("ID:", peca["id"])
            print("Peso:", peca["peso"], "g")
            print("Cor:", peca["cor"])
            print("Comprimento:", peca["comprimento"], "cm")
            print()

    print("PEÇAS REPROVADAS:")

    if len(pecas_reprovadas) == 0:
        print("Nenhuma peça reprovada.")
    else:
        for peca in pecas_reprovadas:
            print("ID:", peca["id"])
            print("Peso:", peca["peso"], "g")
            print("Cor:", peca["cor"])
            print("Comprimento:", peca["comprimento"], "cm")
            print("Motivos:")

            for motivo in peca["motivos"]:
                print("-", motivo)

            print()

def listar_caixas():
    print()
    print("========================================")
    print("          CAIXAS FECHADAS")
    print("========================================")

    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa fechada.")
    else:
        for numero, caixa in enumerate(caixas_fechadas, start=1):
            print()
            print("CAIXA", numero)
            print("Quantidade de peças:", len(caixa))

            for peca in caixa:
                print(
                    "ID:", peca["id"],
                    "| Peso:", peca["peso"], "g",
                    "| Cor:", peca["cor"],
                    "| Comprimento:", peca["comprimento"], "cm"
                )

def remover_peca():
    print()
    print("========================================")
    print("          REMOVER PEÇA")
    print("========================================")

    id_remover = input("Digite o ID da peça que deseja remover: ")

    # Verifica se a peça já está em uma caixa fechada
    for caixa in caixas_fechadas:
        for peca in caixa:
            if peca["id"] == id_remover:
                print("Essa peça já está em uma caixa fechada e não pode ser removida.")
                return

    # Verifica se a peça está entre as aprovadas
    for peca in pecas_aprovadas:
        if peca["id"] == id_remover:
            pecas_aprovadas.remove(peca)

            # Remove também da caixa atual
            for peca_caixa in caixa_atual:
                if peca_caixa["id"] == id_remover:
                    caixa_atual.remove(peca_caixa)
                    break

            print("Peça removida com sucesso.")
            return

    # Verifica se a peça está entre as reprovadas
    for peca in pecas_reprovadas:
        if peca["id"] == id_remover:
            pecas_reprovadas.remove(peca)
            print("Peça removida com sucesso.")
            return

    print("Peça não encontrada.")

def gerar_relatorio():
    print()
    print("========================================")
    print("          RELATÓRIO FINAL")
    print("========================================")

    print()
    print("TOTAL DE PEÇAS APROVADAS:", len(pecas_aprovadas))
    print("TOTAL DE PEÇAS REPROVADAS:", len(pecas_reprovadas))

    print()
    print("PEÇAS REPROVADAS E MOTIVOS:")

    if len(pecas_reprovadas) == 0:
        print("Nenhuma peça reprovada.")
    else:
        for peca in pecas_reprovadas:
            print()
            print("ID:", peca["id"])

            for motivo in peca["motivos"]:
                print("-", motivo)

    caixas_utilizadas = len(caixas_fechadas)

    if len(caixa_atual) > 0:
        caixas_utilizadas = caixas_utilizadas + 1

    print()
    print("QUANTIDADE DE CAIXAS UTILIZADAS:", caixas_utilizadas)
    print("PEÇAS NA CAIXA ATUAL:", len(caixa_atual))

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um valor numérico válido.")

def cadastrar_peca():
    global caixa_atual
    
    print()
    print("========================================")
    print("          CADASTRO DE PEÇA")
    print("========================================")

    id_peca = input("Digite o ID da peça: ").strip()
    
    if id_ja_cadastrado(id_peca):
        print("ID já cadastrado.")
        return

    peso = ler_numero("Digite o peso da peça (g): ")
    
    while True:
        cor = input("Digite a cor da peça: ").strip()

        if cor.replace(".", "", 1).isdigit():
            print("Cor inválida. Digite uma cor.")
        else:
            break
    
    comprimento = ler_numero("Digite o comprimento da peça (cm): ")

    motivos = []

    print()

    if 95 <= peso <= 105:
        print("Peso: APROVADO")
    else:
        print("Peso: REPROVADO")
        motivos.append("Peso fora do padrão")

    if cor.lower() == "azul" or cor.lower() == "verde":
        print("Cor: APROVADA")
    else:
        print("Cor: REPROVADA")
        motivos.append("Cor não permitida")

    if 10 <= comprimento <= 20:
        print("Comprimento: APROVADO")
    else:
        print("Comprimento: REPROVADO")
        motivos.append("Comprimento fora do padrão")

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "motivos": motivos
    }

    if len(motivos) == 0:
        print()
        print("STATUS: PEÇA APROVADA")
        pecas_aprovadas.append(peca)
        caixa_atual.append(peca)
        
        if len(caixa_atual) == 10:
            caixas_fechadas.append(caixa_atual.copy())
            caixa_atual.clear()
            print("Caixa fechada com 10 peças!")
    
    else:
        print()
        print("STATUS: PEÇA REPROVADA")
        print("Motivos:")

        for motivo in motivos:
            print("-", motivo)

        pecas_reprovadas.append(peca)


while True:
    print()
    print("========================================")
    print("   SISTEMA DE CONTROLE DE QUALIDADE")
    print("========================================")
    print()
    print("1 - Cadastrar nova peça")
    print("2 - Listar peças aprovadas/reprovadas")
    print("3 - Remover peça cadastrada")
    print("4 - Listar caixas fechadas")
    print("5 - Gerar relatório final")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_peca()

    elif opcao == "2":
        listar_pecas()

    elif opcao == "3":
        remover_peca()

    elif opcao == "4":
        listar_caixas()

    elif opcao == "5":
        gerar_relatorio()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
