from unidecode import unidecode

def imprimir_boasvindas(nome_da_loja):
    print(f"Bem-vindo a {nome_da_loja}\n")


def imprimir_menu():
    print(f"SELECIONE UMA OPÇÃO ABAIXO:\n\n"
          "  [1] Adicionar novo cliente\n"
          "  [2] Remover cliente\n"
          "  [3] Alterar dados de um cliente\n"
          "  [4] Consultar base de clientes\n"
          "  [5] Registrar compra\n"
          "  [6] Adicionar novo livro ao sistema\n"
          "  [7] Alterar dados de um livro\n"
          "  [8] Remover livro do sistema\n"
          "  [9] Buscar livro")


def solicitar_cpf_cliente():

    print(f"\nDigite o CPF (apenas números).\n"
          f"Ou digite '000' para sair.\n")

    while True:

        cpf = input("CPF: ").replace('-', '').replace(' ', '').replace('.', '')

        if cpf.isdigit() and len(cpf) == 11:
            return cpf

        elif cpf == '000':
            return cpf

        else:
            print("\nVocê digitou um CPF inválido!")

            if not cpf.isdigit():
                print("Digite o CPF no formato 12345678900 (apenas números).")

            elif len(cpf) != 11:
                print(f"Você digitou {len(cpf)} números!\n"
                      f"O CPF deve ter 11 números.")
            print("Se sua intenção era sair, digite '000'.\n")


def solicitar_nome_cliente():

    while True:

        nome = input("\nNome completo do cliente: ").title().strip().replace('  ', ' ')
        nome_sem_espacos = nome.strip().replace(' ', '').replace('  ', '')

        if nome_sem_espacos.isalpha():
            return nome
        else:
            print("\nVocê está inserindo algum caractere especial, insira apenas letras.")
            continue


def solicitar_email_cliente():
    while True:

        email = str(input("\nE-mail do cliente: ")).lower().strip().replace('  ', ' ')

        if not '@' in email and len(email) < 5:
            print("Digite um endereço de e-mail válido!\n"
                  "Você digitou um endereço de e-mail sem '@' e muito curto!")
            continue

        elif not '@' in email:
            print("Digite um endereço de e-mail válido!\n"
                  "Todo e-mail precisa de um '@'.\n")
            continue

        elif len(email) < 5:
            print("Digite um endereço de e-mail válido!\n"
                  "Você digitou um email muito curto.")
            continue

        elif not '@' in email and len(email) < 5:
            print("Digite um endereço de e-mail válido!\n"
                  "Você digitou um endereço de e-mail sem '@' e muito curto!")
            continue

        elif '@' in email:
            return email


def solicitar_telefone_cliente():
    while True:
        telefone = input("\nTelefone do cliente (apenas números, com código de área (DDD) + 9 antes do número): ")

        if telefone.isdigit() and len(telefone) == 11:
            return telefone

        else:
            print("\nVocê digitou um telefone inválido!")

            if not telefone.isdigit():
                print("Digite o telefone no formato correto!\n"
                      "O telefone deve ter apenas números.\n"
                      "Insira no formato com código de área (DDD) + 9 antes do número.\n")

            elif len(telefone) != 11:
                print(f"Você digitou {len(telefone)} números!\n"
                      f"O telefone deve ter 11 números.\n"
                      f"Digite novamente.\n")


def solicitar_valor_compras():
    while True:
        valor_compras = input("\nQual o valor em compras gasto pelo cliente? (Digite 000 para sair):  ")

        try:
            valor_compras = float(valor_compras)

            if valor_compras >= 0:
                return valor_compras
            else:
                print("\nDigite um valor maior que zero.")
                continue

        except ValueError:
            print("Você inseriu algum caractere inválido!\n"
                  "Digite apenas números para o valor em compras!\n")
            continue


def remover_cliente(cpf, dicionario):
    print(f"Cliente {dicionario[cpf]['nome']} removido com sucesso!")
    del dicionario[cpf]


def atribuir_segmento(qtde_total_valor_cliente):
    if qtde_total_valor_cliente == 0:
        segmento = 'Sem status'
        return segmento

    elif 0 < qtde_total_valor_cliente <= 1000:
        segmento = 'Bronze'
        return segmento

    elif 1000 < qtde_total_valor_cliente <= 5000:
        segmento = 'Prata'
        return segmento

    elif 5000 < qtde_total_valor_cliente <= 20000:
        segmento = 'Ouro'
        return segmento

    elif qtde_total_valor_cliente > 20000:
        segmento = 'Diamante'
        return segmento


def alterar_dados_cliente(cpf, dicionario):
    dado_a_alterar = input(f"Qual dado deseja alterar do cliente {dicionario[cpf]['nome']}?\n\n"
                           f"  [1] CPF\n"
                           f"  [2] NOME\n"
                           f"  [3] E-MAIL\n"
                           f"  [4] TELEFONE\n"
                           f"  [5] VALOR EM COMPRAS\n").strip()

    if dado_a_alterar == '1':
        while True:
            novo_cpf = solicitar_cpf_cliente()

            if novo_cpf == '000':
                break

            else:
                try:
                    dicionario[novo_cpf] = dicionario.pop(cpf)
                except KeyError:
                    print("\nCPF não encontrado!")
                except ValueError:
                    print("\nDigite apenas números de CPF. (Ex: 12345678900")

    elif dado_a_alterar == '2':

        novo_nome = solicitar_nome_cliente()

        dicionario[cpf]['nome'] = novo_nome

    elif dado_a_alterar == '3':

        novo_email = solicitar_email_cliente()

        dicionario[cpf]['email'] = novo_email

    elif dado_a_alterar == '4':

        novo_telefone = solicitar_telefone_cliente()

        dicionario[cpf]['telefone'] = novo_telefone

    elif dado_a_alterar == '5':

        novo_valor_total_compras = float(input("\nDigite o novo valor total em compras: "))
        dicionario[cpf]['valor_total_compras'] = novo_valor_total_compras
        novo_segmento = atribuir_segmento(novo_valor_total_compras)
        dicionario[cpf]['segmento'] = novo_segmento


def adicionar_valor_de_compra(cpf, dicionario):
    while True:
        print(f"Valor acumulado do cliente {dicionario[cpf]['nome']}: R${dicionario[cpf]['valor_total_compras']:,.2f}")
        valor_a_adicionar = input(f"\nDigite o valor a ser adicionado ao valor total de compras do cliente: ")
        try:
            valor_a_adicionar = float(valor_a_adicionar)

            if valor_a_adicionar >= 0:
                dicionario[cpf]['valor_total_compras'] += valor_a_adicionar

            else:
                print("\nDigite um valor maior que zero.")
                continue

        except ValueError:
            print("Você inseriu algum caractere inválido!\n"
                  "Digite apenas números para o valor em compras!\n")
            continue


def ver_base_de_dados_clientes(dicionario):
    for cpf, dados in dicionario.items():
        nome = dados['nome']
        email = dados['email']
        telefone = dados['telefone']
        valor_total_compras = dados['valor_total_compras']
        segmento = dados['segmento']
        livros_comprados = dados.get('livros_comprados', 'Nenhum livro comprado.')

        print(f"\n"
              f"-----------------------------\n"
              f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\n"
              f"-----------------------------\n"
              f"Nome: {nome}\n"
              f"E-mail: {email}\n"
              f"Telefone: ({telefone[:2]}) {telefone[2:3]} {telefone[3:7]}-{telefone[7:]}\n"
              f"Valor total em compras: R${valor_total_compras:,.2f}\n"
              f"Status do cliente: {segmento}\n")

        print(f"Livros comprados:")

        if livros_comprados != {}:
            for id_livro, dados in livros_comprados.items():
                nome_livro = dados['nome_do_livro']
                qtde_comprada = dados['qtde_comprada_do_livro']
                print(f"Nome: {nome_livro}\n"
                      f"ID: {id_livro}\n"
                      f"Quantidade comprada: {qtde_comprada}\n"
                      f"-----------------------------")

        else:
            print("Nenhum livro comprado.")
            print()


def adicionar_livro(dicionario_livros):

    id_livro = max(dicionario_livros) + 1

    nome_livro = input("\nDigite o nome do livro a ser adicionado: ").strip()

    genero = input("\nDigite o gênero do livro a ser adicionado: ").strip().capitalize()

    autor = input("\nDigite o nome do autor do livro a ser adicionado: ").strip().title()

    ano_lancamento = int(input("\nDigite o ano de lançamento do livro: "))

    preco = float(input("\nDigite o preço do livro: "))

    qtde_disponivel = int(input("\nDigite a quantidade disponível do livro: "))

    dicionario_livros[id_livro] = {
        'nome_do_livro': nome_livro,
        'autor': autor,
        'genero': genero,
        'lancamento': ano_lancamento,
        'qtde_disponivel': qtde_disponivel,
        'preço': preco}

    print("\nLivro adicionado com sucesso!\n")


def alterar_dados_livro(dicionario_livros):

    while True:

        print("\nDe qual livro você deseja alterar os dados?\n"
                      "  [1] Buscar por ID\n"
                      "  [2] Buscar pelo nome\n")

        opcao = input("Digite o número referente a opção desejada ('000' para sair): ")

        print()

        if opcao == '1':
            id_livro = int(input("Digite o ID do livro que deseja alterar ('000' para sair): "))

            print()

            if id_livro in dicionario_livros:
                livro_info = dicionario_livros[id_livro]
                print("Detalhes do livro selecionado:")
                print(f"ID: {id_livro}\n"
                      f"Nome: {livro_info['nome_do_livro']}\n"
                      f"Autor: {livro_info['autor']}\n"
                      f"Gênero: {livro_info['genero']}\n")

                confirmacao = input("Esse é o livro que você deseja alterar os dados? [S/N]: ").upper().strip()

                if confirmacao == 'S':

                    print()

                    while True:

                        print("Qual dado deseja alterar?\n\n"
                              "  [1] Nome do livro\n"
                              "  [2] Autor\n"
                              "  [3] Gênero\n"
                              "  [4] Ano de lançamento\n"
                              "  [5] Quantidade disponível\n"
                              "  [6] Preço\n")

                        selecionar_info = input("Digite o número referente a opção desejada ('000' para sair): ")
                        print()

                        while selecionar_info not in ['1', '2', '3', '4', '5', '6', '000']:
                            print("Selecione uma opção válida!\n")
                            print("Qual dado deseja alterar?\n\n"
                                  "  [1] Nome do livro\n"
                                  "  [2] Autor\n"
                                  "  [3] Gênero\n"
                                  "  [4] Ano de lançamento\n"
                                  "  [5] Quantidade disponível\n"
                                  "  [6] Preço\n")

                            selecionar_info = input("Digite o número referente a opção desejada ('000' para sair): ")
                            print()


                        if selecionar_info == '1':

                            novo_nome = input(f"Digite o novo nome para o livro '{livro_info['nome_do_livro']}' ('000' para sair): ").title()

                            print()

                            if novo_nome == '000':
                                break

                            else:

                                confirmacao_alteracao = input(f"Deseja realmente alterar o nome de '{livro_info['nome_do_livro']}' para '{novo_nome}' [S/N]? ").upper()

                                print()

                                if confirmacao_alteracao == 'S':
                                    print(f"Nome atualizado de '{livro_info['nome_do_livro']}' para '{novo_nome}' com sucesso!")
                                    livro_info['nome_do_livro'] = novo_nome
                                    print()
                                    continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                    while continuar_alterando not in ['S', 'N']:
                                        print("\nDigite uma opção válida! [S/N]\n")
                                        continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                    if continuar_alterando == 'S':
                                        print()
                                        continue

                                    elif continuar_alterando == 'N':
                                        print()
                                        break

                                else:
                                    break


                        elif selecionar_info == '2':

                            novo_autor = input(f"Digite o novo autor para o livro '{livro_info['nome_do_livro']}' ('000' para sair): ").title()

                            print()

                            if novo_autor == '000':
                                break

                            else:

                                confirmacao_alteracao = input(f"Deseja realmente alterar o autor de '{livro_info['autor']}' para '{novo_autor}' [S/N]? ").upper()

                                print()

                                if confirmacao_alteracao == 'S':

                                    print(f"Autor atualizado de '{livro_info['autor']}' para '{novo_autor}' com sucesso!")
                                    livro_info['autor'] = novo_autor
                                    print()
                                    continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                    while continuar_alterando not in ['S', 'N']:
                                        print("\nDigite uma opção válida! [S/N]\n")
                                        continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                    if continuar_alterando == 'S':
                                        print()
                                        continue

                                    elif continuar_alterando == 'N':
                                        print()
                                        break

                                else:
                                    break

                        elif selecionar_info == '3':

                            novo_genero = input(f"Digite o novo genero para o livro '{livro_info['nome_do_livro']}' ('000' para sair): ").title()

                            print()

                            if novo_genero == '000':
                                break

                            else:

                                confirmacao_alteracao = input(f"Deseja realmente alterar o gênero de '{livro_info['genero']}' para '{novo_genero}' [S/N]? ").upper()

                                if confirmacao_alteracao == 'S':

                                    print(f"\nAutor atualizado de '{livro_info['genero']}' para '{novo_genero}' com sucesso!")
                                    livro_info['genero'] = novo_genero
                                    print()
                                    continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                    while continuar_alterando not in ['S', 'N']:
                                        print("\nDigite uma opção válida! [S/N]\n")
                                        continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                    if continuar_alterando == 'S':
                                        print()
                                        continue

                                    elif continuar_alterando == 'N':
                                        print()
                                        break

                                else:
                                    break


                        elif selecionar_info == '4':
                            try:
                                novo_lancamento = int(input(f"Digite o novo ano de lançamento para o livro '{livro_info['nome_do_livro']}' ('000' para sair): "))

                                print()

                                if novo_lancamento == 000:
                                    break

                                else:

                                    confirmacao_alteracao = input(f"Deseja realmente alterar o ano de lançamento de '{livro_info['lancamento']}' para '{novo_lancamento}' [S/N]? ").upper()
                                    print()

                                    if confirmacao_alteracao == 'S':

                                        print(f"Ano de lançamento atualizado de '{livro_info['lancamento']}' para '{novo_lancamento}' com sucesso!")
                                        livro_info['lancamento'] = novo_lancamento
                                        print()
                                        continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        while continuar_alterando not in ['S', 'N']:
                                            print("\nDigite uma opção válida! [S/N]\n")
                                            continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        if continuar_alterando == 'S':
                                            print()
                                            continue

                                        elif continuar_alterando == 'N':
                                            print()
                                            break

                                    else:
                                        break

                            except ValueError:
                                print("Insira um valor no formato de ano, sem caracteres especiais.")
                                continue

                        elif selecionar_info == '5':
                            try:
                                nova_qtde_disponivel = int(input(f"Digite a nova quantidade disponível para o livro '{livro_info['nome_do_livro']}' ('000' para sair): "))

                                print()

                                if nova_qtde_disponivel == 000:
                                    break

                                else:

                                    confirmacao_alteracao = input(f"Deseja realmente alterar a quantidade disponível de '{livro_info['qtde_disponivel']}' para '{nova_qtde_disponivel}' [S/N]? ").upper()

                                    if confirmacao_alteracao == 'S':
                                        print()
                                        print(f"Quantidade disponível atualizada de '{livro_info['qtde_disponivel']}' para '{nova_qtde_disponivel}' com sucesso!")
                                        livro_info['qtde_disponivel'] = nova_qtde_disponivel
                                        print()
                                        continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        while continuar_alterando not in ['S', 'N']:
                                            print("\nDigite uma opção válida! [S/N]\n")
                                            continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        if continuar_alterando == 'S':
                                            print()
                                            continue

                                        elif continuar_alterando == 'N':
                                            print()
                                            break

                                    else:
                                        break

                            except ValueError:
                                print("Insira uma quantidade válida, sem caracteres especiais.\n")
                                continue

                        elif selecionar_info == '6':
                            try:
                                novo_preco = float(input(f"Digite o novo preço para o livro {livro_info['nome_do_livro']} ('000' para sair): "))

                                print()

                                if novo_preco == 000:
                                    break

                                else:

                                    confirmacao_alteracao = input(f"Deseja realmente alterar o preço de 'R${livro_info['preço']:,.2f}' para 'R${novo_preco:,.2f}' [S/N]? ").upper()

                                    if confirmacao_alteracao == 'S':
                                        print()
                                        print(f"\nPreço atualizado de 'R${livro_info['preço']:,.2f}' para 'R${novo_preco:,.2f}' com sucesso!")
                                        livro_info['preço'] = novo_preco
                                        print()
                                        continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        while continuar_alterando not in ['S', 'N']:
                                            print("\nDigite uma opção válida! [S/N]\n")
                                            continuar_alterando = input("Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        if continuar_alterando == 'S':
                                            print()
                                            continue

                                        elif continuar_alterando == 'N':
                                            print()
                                            break

                                    else:
                                        break

                            except ValueError:
                                print("Insira um valor apenas com números e pontos, em caso de valor com centavos.")
                                continue

                        elif selecionar_info == '000':
                            print("\nAlteração de dados de livros cancelada!\n")
                            break
                        break
                    break

                else:
                    print()
                    print("Remoção cancelada.")

            elif id_livro == 000:
                break

            else:
                print("ID do livro não encontrado.")

        elif opcao == '2':
            palavra_chave = input("Digite a palavra-chave/parte do nome do livro que deseja remover: ")
            resultados = buscar_livros(dicionario_livros, palavra_chave=palavra_chave)

            if resultados:
                print()
                print("Livros encontrados:")
                for livro_id, livro_info in resultados:
                    print(f"ID: {livro_id}\n"
                          f"Nome: {livro_info['nome_do_livro']}\n"
                          f"Autor: {livro_info['autor']}\n"
                          f"Gênero: {livro_info['genero']}\n")

                id_livro = int(input("Digite o ID do livro que deseja alterar ('000' para sair): "))

                print()

                if id_livro in dicionario_livros:
                    livro_info = dicionario_livros[id_livro]
                    print("Detalhes do livro selecionado:")
                    print(f"ID: {id_livro}\n"
                          f"Nome: {livro_info['nome_do_livro']}\n"
                          f"Autor: {livro_info['autor']}\n"
                          f"Gênero: {livro_info['genero']}\n")

                    confirmacao = input("Esse é o livro que você deseja alterar os dados? [S/N]: ").upper().strip()

                    if confirmacao == 'S':

                        print()

                        while True:

                            print("Qual dado deseja alterar?\n\n"
                                  "  [1] Nome do livro\n"
                                  "  [2] Autor\n"
                                  "  [3] Gênero\n"
                                  "  [4] Ano de lançamento\n"
                                  "  [5] Quantidade disponível\n"
                                  "  [6] Preço\n")

                            selecionar_info = input("Digite o número referente a opção desejada ('000' para sair): ")
                            print()

                            while selecionar_info not in ['1', '2', '3', '4', '5', '6', '000']:
                                print("Selecione uma opção válida!\n")
                                print("Qual dado deseja alterar?\n\n"
                                      "  [1] Nome do livro\n"
                                      "  [2] Autor\n"
                                      "  [3] Gênero\n"
                                      "  [4] Ano de lançamento\n"
                                      "  [5] Quantidade disponível\n"
                                      "  [6] Preço\n")

                                selecionar_info = input(
                                    "Digite o número referente a opção desejada ('000' para sair): ")
                                print()

                            if selecionar_info == '1':

                                novo_nome = input(
                                    f"Digite o novo nome para o livro '{livro_info['nome_do_livro']}' ('000' para sair): ").title()

                                print()

                                if novo_nome == '000':
                                    break

                                else:

                                    confirmacao_alteracao = input(
                                        f"Deseja realmente alterar o nome de '{livro_info['nome_do_livro']}' para '{novo_nome}' [S/N]? ").upper()

                                    print()

                                    if confirmacao_alteracao == 'S':
                                        print(
                                            f"Nome atualizado de '{livro_info['nome_do_livro']}' para '{novo_nome}' com sucesso!")
                                        livro_info['nome_do_livro'] = novo_nome
                                        print()
                                        continuar_alterando = input(
                                            "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        while continuar_alterando not in ['S', 'N']:
                                            print("\nDigite uma opção válida! [S/N]\n")
                                            continuar_alterando = input(
                                                "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        if continuar_alterando == 'S':
                                            print()
                                            continue

                                        elif continuar_alterando == 'N':
                                            print()
                                            break

                                    else:
                                        break


                            elif selecionar_info == '2':

                                novo_autor = input(
                                    f"Digite o novo autor para o livro '{livro_info['nome_do_livro']}' ('000' para sair): ").title()

                                print()

                                if novo_autor == '000':
                                    break

                                else:

                                    confirmacao_alteracao = input(
                                        f"Deseja realmente alterar o autor de '{livro_info['autor']}' para '{novo_autor}' [S/N]? ").upper()

                                    print()

                                    if confirmacao_alteracao == 'S':

                                        print(
                                            f"Autor atualizado de '{livro_info['autor']}' para '{novo_autor}' com sucesso!")
                                        livro_info['autor'] = novo_autor
                                        print()
                                        continuar_alterando = input(
                                            "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        while continuar_alterando not in ['S', 'N']:
                                            print("\nDigite uma opção válida! [S/N]\n")
                                            continuar_alterando = input(
                                                "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        if continuar_alterando == 'S':
                                            print()
                                            continue

                                        elif continuar_alterando == 'N':
                                            print()
                                            break

                                    else:
                                        break

                            elif selecionar_info == '3':

                                novo_genero = input(
                                    f"Digite o novo genero para o livro '{livro_info['nome_do_livro']}' ('000' para sair): ").title()

                                print()

                                if novo_genero == '000':
                                    break

                                else:

                                    confirmacao_alteracao = input(
                                        f"Deseja realmente alterar o gênero de '{livro_info['genero']}' para '{novo_genero}' [S/N]? ").upper()

                                    if confirmacao_alteracao == 'S':

                                        print(
                                            f"\nAutor atualizado de '{livro_info['genero']}' para '{novo_genero}' com sucesso!")
                                        livro_info['genero'] = novo_genero
                                        print()
                                        continuar_alterando = input(
                                            "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        while continuar_alterando not in ['S', 'N']:
                                            print("\nDigite uma opção válida! [S/N]\n")
                                            continuar_alterando = input(
                                                "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                        if continuar_alterando == 'S':
                                            print()
                                            continue

                                        elif continuar_alterando == 'N':
                                            print()
                                            break

                                    else:
                                        break


                            elif selecionar_info == '4':
                                try:
                                    novo_lancamento = int(input(
                                        f"Digite o novo ano de lançamento para o livro '{livro_info['nome_do_livro']}' ('000' para sair): "))

                                    print()

                                    if novo_lancamento == 000:
                                        break

                                    else:

                                        confirmacao_alteracao = input(
                                            f"Deseja realmente alterar o ano de lançamento de '{livro_info['lancamento']}' para '{novo_lancamento}' [S/N]? ").upper()
                                        print()

                                        if confirmacao_alteracao == 'S':

                                            print(
                                                f"Ano de lançamento atualizado de '{livro_info['lancamento']}' para '{novo_lancamento}' com sucesso!")
                                            livro_info['lancamento'] = novo_lancamento
                                            print()
                                            continuar_alterando = input(
                                                "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                            while continuar_alterando not in ['S', 'N']:
                                                print("\nDigite uma opção válida! [S/N]\n")
                                                continuar_alterando = input(
                                                    "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                            if continuar_alterando == 'S':
                                                print()
                                                continue

                                            elif continuar_alterando == 'N':
                                                print()
                                                break

                                        else:
                                            break

                                except ValueError:
                                    print("Insira um valor no formato de ano, sem caracteres especiais.")
                                    continue

                            elif selecionar_info == '5':
                                try:
                                    nova_qtde_disponivel = int(input(
                                        f"Digite a nova quantidade disponível para o livro '{livro_info['nome_do_livro']}' ('000' para sair): "))

                                    print()

                                    if nova_qtde_disponivel == 000:
                                        break

                                    else:

                                        confirmacao_alteracao = input(
                                            f"Deseja realmente alterar a quantidade disponível de '{livro_info['qtde_disponivel']}' para '{nova_qtde_disponivel}' [S/N]? ").upper()

                                        if confirmacao_alteracao == 'S':
                                            print()
                                            print(
                                                f"Quantidade disponível atualizada de '{livro_info['qtde_disponivel']}' para '{nova_qtde_disponivel}' com sucesso!")
                                            livro_info['qtde_disponivel'] = nova_qtde_disponivel
                                            print()
                                            continuar_alterando = input(
                                                "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                            while continuar_alterando not in ['S', 'N']:
                                                print("\nDigite uma opção válida! [S/N]\n")
                                                continuar_alterando = input(
                                                    "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                            if continuar_alterando == 'S':
                                                print()
                                                continue

                                            elif continuar_alterando == 'N':
                                                print()
                                                break

                                        else:
                                            break

                                except ValueError:
                                    print("Insira uma quantidade válida, sem caracteres especiais.\n")
                                    continue

                            elif selecionar_info == '6':
                                try:
                                    novo_preco = float(input(
                                        f"Digite o novo preço para o livro {livro_info['nome_do_livro']} ('000' para sair): "))

                                    print()

                                    if novo_preco == 000:
                                        break

                                    else:

                                        confirmacao_alteracao = input(
                                            f"Deseja realmente alterar o preço de 'R${livro_info['preço']:,.2f}' para 'R${novo_preco:,.2f}' [S/N]? ").upper()

                                        if confirmacao_alteracao == 'S':
                                            print()
                                            print(
                                                f"\nPreço atualizado de 'R${livro_info['preço']:,.2f}' para 'R${novo_preco:,.2f}' com sucesso!")
                                            livro_info['preço'] = novo_preco
                                            print()
                                            continuar_alterando = input(
                                                "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                            while continuar_alterando not in ['S', 'N']:
                                                print("\nDigite uma opção válida! [S/N]\n")
                                                continuar_alterando = input(
                                                    "Deseja continuar alterando os dados deste livro? [S/N]").upper()

                                            if continuar_alterando == 'S':
                                                print()
                                                continue

                                            elif continuar_alterando == 'N':
                                                print()
                                                break

                                        else:
                                            break

                                except ValueError:
                                    print("Insira um valor apenas com números e pontos, em caso de valor com centavos.")
                                    continue

                            elif selecionar_info == '000':
                                print("\nAlteração de dados de livros cancelada!\n")
                                break
                            break
                        break

                    else:
                        print()
                        print("Remoção cancelada.")

                elif id_livro == 000:
                    break

                else:
                    print("ID do livro não encontrado.")

        elif opcao == '000':
            break


def remover_livro(dicionario_livros):
    opcao = input("Digite 1 para apagar pelo ID e 2 para apagar pelo nome: ")

    if opcao == '1':
        id_livro = int(input("Digite o ID do livro que deseja remover: "))

        if id_livro in dicionario_livros:
            livro_info = dicionario_livros[id_livro]
            print("Detalhes do livro encontrado:")
            print(f"ID: {id_livro}\n"
                  f"Nome: {livro_info['nome_do_livro']}\n"
                  f"Autor: {livro_info['autor']}\n"
                  f"Gênero: {livro_info['genero']}\n")

            confirmacao = input("Deseja realmente remover o livro? (S/N): ").upper().strip()

            if confirmacao == 'S':
                del dicionario_livros[id_livro]
                print("Livro removido com sucesso! Esta ação é irreversível.")
            else:
                print("Remoção cancelada.")

        else:
            print("ID do livro não encontrado.")

    elif opcao == '2':
        palavra_chave = input("Digite a palavra-chave/parte do nome do livro que deseja remover: ")
        resultados = buscar_livros(dicionario_livros, palavra_chave=palavra_chave)

        if resultados:
            print("Livros encontrados:")
            for livro_id, livro_info in resultados:
                print(f"ID: {livro_id}\n"
                      f"Nome: {livro_info['nome_do_livro']}\n"
                      f"Autor: {livro_info['autor']}\n"
                      f"Gênero: {livro_info['genero']}\n")

            id_livro = int(input("Digite o ID referente ao livro que deseja remover: "))

            if id_livro in dicionario_livros:
                livro_info = dicionario_livros[id_livro]
                print("Detalhes do livro encontrado:")
                print(f"ID: {id_livro}\n"
                      f"Nome: {livro_info['nome_do_livro']}\n"
                      f"Autor: {livro_info['autor']}\n"
                      f"Gênero: {livro_info['genero']}\n")

                confirmacao = input("Deseja realmente remover o livro acima? (S/N): ").upper().strip()
                if confirmacao == 'S':
                    del dicionario_livros[id_livro]
                    print("Livro removido com sucesso! Esta ação é irreversível.")
                else:
                    print("Remoção cancelada.")
            else:
                print("ID do livro não encontrado.")
        else:
            print("Nenhum livro encontrado com a palavra-chave fornecida.")

    else:
        print("Opção inválida.")


def buscar_livros(dicionario_livros, palavra_chave=None, genero=None, autor=None):
    resultados = []

    for livro_id, livro_info in dicionario_livros.items():
        if palavra_chave:
            palavras_no_nome = unidecode(livro_info['nome_do_livro'].lower()).split()
            if unidecode(palavra_chave.lower()) in palavras_no_nome:
                resultados.append((livro_id, livro_info))
        elif genero and unidecode(genero.lower()) == unidecode(livro_info['genero'].lower()):
            resultados.append((livro_id, livro_info))
        elif autor and unidecode(autor.lower()) in unidecode(livro_info['autor'].lower()):
            resultados.append((livro_id, livro_info))

    return resultados


def registrar_compra(cpf, dicionario_clientes, dicionario_livros):
    print()

    while True:
        print("Deseja buscar o livro de qual maneira?\n"
              "  [1] Buscar pelo ID\n"
              "  [2] Buscar pelo nome\n")

        opcao = input("Opção de busca desejada: ")

        if opcao == '1':
            print()
            id_livro = int(input("Digite o ID do livro que deseja registrar a compra ('000' para sair): "))
            print()

            if id_livro in dicionario_livros:
                livro_info = dicionario_livros[id_livro]

                if livro_info['qtde_disponivel'] == 0:
                    print(f"Livro '{livro_info['nome_do_livro']}' indisponível em estoque.\n\n"
                          f"Tente outro livro\n")
                    continue

                else:
                    print("Detalhes do livro selecionado:\n")
                    print(f"ID: {id_livro}\n"
                          f"Nome: {livro_info['nome_do_livro']}\n"
                          f"Autor: {livro_info['autor']}\n"
                          f"Gênero: {livro_info['genero']}\n"
                          f"Qtde disponível: {livro_info['qtde_disponivel']}\n"
                          f"Preço: R${livro_info['preço']:,.2f}\n")

                    confirmacao = input("Esse é o livro que você quer registrar a compra? [S/N]: ").upper().strip()

                    if confirmacao == 'S':

                        livro_a_comprar = dicionario_livros[id_livro]

                        while True:
                            qtde_a_comprar = int(input("\nDigite a quantidade será comprada do livro: "))

                            if qtde_a_comprar <= livro_a_comprar['qtde_disponivel']:

                                if id_livro not in dicionario_clientes[cpf]['livros_comprados']:

                                    livro_comprado = {
                                        'id': id_livro,
                                        'nome_do_livro': livro_a_comprar['nome_do_livro'],
                                        'qtde_comprada_do_livro': qtde_a_comprar,
                                        'preço_unitario': livro_a_comprar['preço'],
                                        'valor_total_pago': livro_a_comprar['preço'] * qtde_a_comprar}

                                    dicionario_clientes[cpf]['livros_comprados'][id_livro] = livro_comprado

                                    dicionario_clientes[cpf]['valor_total_compras'] += (livro_a_comprar['preço'] * qtde_a_comprar)

                                    livro_a_comprar['qtde_disponivel'] -= qtde_a_comprar

                                    dicionario_clientes[cpf]['segmento'] = atribuir_segmento(
                                        dicionario_clientes[cpf]['valor_total_compras'])

                                    print("\nCompra registrada com sucesso!\n")

                                    break

                                elif id_livro in dicionario_clientes[cpf]['livros_comprados']:
                                    print("\nCliente já comprou este livro.")

                                    confirmacao = input("Cliente deseja comprar novamente o mesmo livro? [S/N]: ").strip().upper()

                                    if confirmacao == 'S':
                                        livro_a_comprar['qtde_disponivel'] -= qtde_a_comprar

                                        dicionario_clientes[cpf]['livros_comprados'][id_livro][
                                            'qtde_comprada_do_livro'] += qtde_a_comprar

                                        dicionario_clientes[cpf]['valor_total_compras'] += (
                                                    livro_a_comprar['preço'] * qtde_a_comprar)

                                        dicionario_clientes[cpf]['segmento'] = atribuir_segmento(
                                            dicionario_clientes[cpf]['valor_total_compras'])

                                        print("Compra registrada com sucesso!\n")

                                        break

                                    if confirmacao == 'N':
                                        print("\nCompra cancelada!\n")
                                        break

                            elif qtde_a_comprar > livro_a_comprar['qtde_disponivel']:
                                print(f"\nQuantidade indisponível desse livro.\n"
                                      f"Quantidade do livro em estoque: {livro_a_comprar['qtde_disponivel']}")
                                continue

                    elif confirmacao == 'N':
                        print("\nVamos tentar novamente.\n")
                        continue

                    else:
                        print("Digite uma opção válida! [S/N]")
                        continue

            else:
                print("Livro não encontrado!")
                continue



        elif opcao == '2':
            print()
            palavra_chave = input("Digite a palavra-chave/parte do nome do livro que você está buscando: ")

            resultados = buscar_livros(dicionario_livros, palavra_chave=palavra_chave)

            if resultados:

                print()

                print("Livros encontrados:\n")

                for livro_id, livro_info in resultados:
                    print(f"ID: {livro_id}\n"
                          f"Nome: {livro_info['nome_do_livro']}\n"
                          f"Autor: {livro_info['autor']}\n"
                          f"Gênero: {livro_info['genero']}\n"
                          f"Qtde disponível: {livro_info['qtde_disponivel']}\n"
                          f"Preço: R${livro_info['preço']:,.2f}\n")

                id_livro = int(input("Digite o ID do livro que deseja registrar a compra ('000' para sair): "))

                print()

                if id_livro in dicionario_livros:
                    livro_info = dicionario_livros[id_livro]

                    if livro_info['qtde_disponivel'] == 0:
                        print(f"Livro '{livro_info['nome_do_livro']}' indisponível em estoque.\n\n"
                              f"Tente outro livro!\n")
                        continue

                    else:
                        print("Detalhes do livro selecionado:\n")
                        print(f"ID: {id_livro}\n"
                              f"Nome: {livro_info['nome_do_livro']}\n"
                              f"Autor: {livro_info['autor']}\n"
                              f"Gênero: {livro_info['genero']}\n"
                              f"Qtde disponível: {livro_info['qtde_disponivel']}\n"
                              f"Preço: R${livro_info['preço']:,.2f}\n")

                        confirmacao = input("Esse é o livro que você quer registrar a compra? [S/N]: ").upper().strip()

                        if confirmacao == 'S':

                            livro_a_comprar = dicionario_livros[id_livro]

                            while True:
                                print()
                                qtde_a_comprar = int(input("Digite a quantidade será comprada do livro: "))

                                if qtde_a_comprar <= livro_a_comprar['qtde_disponivel']:

                                    if id_livro not in dicionario_clientes[cpf]['livros_comprados']:

                                        livro_comprado = {
                                            'id': id_livro,
                                            'nome_do_livro': livro_a_comprar['nome_do_livro'],
                                            'qtde_comprada_do_livro': qtde_a_comprar,
                                            'preço_unitario': livro_a_comprar['preço'],
                                            'valor_total_pago': livro_a_comprar['preço'] * qtde_a_comprar}

                                        dicionario_clientes[cpf]['livros_comprados'][id_livro] = livro_comprado

                                        dicionario_clientes[cpf]['valor_total_compras'] += (livro_a_comprar['preço'] * qtde_a_comprar)

                                        livro_a_comprar['qtde_disponivel'] -= qtde_a_comprar

                                        dicionario_clientes[cpf]['segmento'] = atribuir_segmento(dicionario_clientes[cpf]['valor_total_compras'])

                                        print("\nCompra registrada com sucesso!\n")

                                        break


                                    elif id_livro in dicionario_clientes[cpf]['livros_comprados']:
                                        print("\nCliente já comprou este livro.\n")

                                        confirmacao = input("Cliente deseja comprar novamente o mesmo livro? [S/N]: ").strip().upper()

                                        if confirmacao == 'S':
                                            livro_a_comprar['qtde_disponivel'] -= qtde_a_comprar

                                            dicionario_clientes[cpf]['livros_comprados'][id_livro]['qtde_comprada_do_livro'] += qtde_a_comprar

                                            dicionario_clientes[cpf]['valor_total_compras'] += (livro_a_comprar['preço'] * qtde_a_comprar)

                                            dicionario_clientes[cpf]['segmento'] = atribuir_segmento(dicionario_clientes[cpf]['valor_total_compras'])

                                            print("\nCompra registrada com sucesso!\n")

                                            break

                                        elif confirmacao == 'N':
                                            print("\nCompra cancelada!\n")
                                            break

                                elif qtde_a_comprar > livro_a_comprar['qtde_disponivel']:
                                    print(f"Quantidade indisponível desse livro.\n"
                                          f"Quantidade do livro em estoque: {livro_a_comprar['qtde_disponivel']}")
                                    continue
                                break

                        elif confirmacao == 'N':
                            print("\nVamos tentar novamente.\n")
                            continue

                else:
                    print("Livro não encontrado!")
                    continue

            else:
                print("Nenhum livro encontrado.")
                continue
        else:
            print("\nDigite uma opção válida! [1 ou 2]\n")
            continue

        mais_compras = input("Deseja fazer mais compras? [S/N]: ").strip().upper()
        if mais_compras != 'S':
            break  # Sair do loop externo se o usuário não deseja fazer mais compras


dicionario_cpf_nomecliente_valorcompras_segmento = {}

imprimir_boasvindas('Livrarias Teste')

dicionario_livros = {
    1: {'nome_do_livro': 'A Viagem do Peregrino da Alvorada',
        'autor': 'John Smith',
        'genero': 'Ficção Científica',
        'lancamento': 1992,
        'qtde_disponivel': 28,
        'preço': 75.50},
    2: {'nome_do_livro': 'O Mistério do Colar Desaparecido',
        'autor': 'Sophia Thompson',
        'genero': 'Drama',
        'lancamento': 1985,
        'qtde_disponivel': 3,
        'preço': 110.20},
    3: {'nome_do_livro': 'O Último Feiticeiro',
        'autor': 'Jennifer Brown',
        'genero': 'Romance',
        'lancamento': 1999,
        'qtde_disponivel': 42,
        'preço': 18.75},
    4: {'nome_do_livro': 'A Luz do Saber',
        'autor': 'Matthew Wilson',
        'genero': 'Mistério',
        'lancamento': 1977,
        'qtde_disponivel': 0,
        'preço': 54.30},
    5: {'nome_do_livro': 'As Crônicas do Abismo',
        'autor': 'Christopher Wilson',
        'genero': 'Aventura',
        'lancamento': 1982,
        'qtde_disponivel': 17,
        'preço': 92.60},
    6: {'nome_do_livro': 'A Busca pelo Tesouro Perdido',
        'autor': 'Emma Williams',
        'genero': 'Thriller',
        'lancamento': 2005,
        'qtde_disponivel': 29,
        'preço': 23.45},
    7: {'nome_do_livro': 'No Limiar da Escuridão',
        'autor': 'David Harris',
        'genero': 'História',
        'lancamento': 1988,
        'qtde_disponivel': 11,
        'preço': 101.80},
    8: {'nome_do_livro': 'Além do Horizonte',
        'autor': 'Brian Miller',
        'genero': 'Fantasia',
        'lancamento': 2002,
        'qtde_disponivel': 7,
        'preço': 49.90},
    9: {'nome_do_livro': 'A Chave do Destino',
        'autor': 'Sophia Thompson',
        'genero': 'Romance',
        'lancamento': 1995,
        'qtde_disponivel': 13,
        'preço': 67.15},
    10: {'nome_do_livro': 'A Sombra do Passado',
         'autor': 'Jennifer Brown',
         'genero': 'Mistério',
         'lancamento': 1979,
         'qtde_disponivel': 0,
         'preço': 88.40},
    11: {'nome_do_livro': 'O Enigma do Labirinto',
         'autor': 'Christopher Wilson',
         'genero': 'Aventura',
         'lancamento': 1998,
         'qtde_disponivel': 20,
         'preço': 45.70},
    12: {'nome_do_livro': 'O Segredo da Cidade Submersa',
         'autor': 'Matthew Wilson',
         'genero': 'Fantasia',
         'lancamento': 1990,
         'qtde_disponivel': 6,
         'preço': 67.80},
    13: {'nome_do_livro': 'A Trilha da Esperança',
         'autor': 'Emma Williams',
         'genero': 'Drama',
         'lancamento': 1983,
         'qtde_disponivel': 19,
         'preço': 36.25},
    14: {'nome_do_livro': 'Os Destemidos',
         'autor': 'Brian Miller',
         'genero': 'Ficção Científica',
         'lancamento': 1993,
         'qtde_disponivel': 0,
         'preço': 19.70},
    15: {'nome_do_livro': 'O Refúgio das Sombras',
         'autor': 'David Harris',
         'genero': 'Thriller',
         'lancamento': 1986,
         'qtde_disponivel': 26,
         'preço': 78.90},
    16: {'nome_do_livro': 'A Herança do Tempo',
         'autor': 'Sophia Thompson',
         'genero': 'Fantasia',
         'lancamento': 1981,
         'qtde_disponivel': 12,
         'preço': 22.50},
    17: {'nome_do_livro': 'O Código da Serpente',
         'autor': 'Jennifer Brown',
         'genero': 'Mistério',
         'lancamento': 1975,
         'qtde_disponivel': 37,
         'preço': 55.80},
    18: {'nome_do_livro': 'O Despertar do Dragão',
         'autor': 'Matthew Wilson',
         'genero': 'Aventura',
         'lancamento': 1984,
         'qtde_disponivel': 0,
         'preço': 32.40},
    19: {'nome_do_livro': 'O Reino Perdido',
         'autor': 'Brian Miller',
         'genero': 'Fantasia',
         'lancamento': 2001,
         'qtde_disponivel': 41,
         'preço': 74.60},
    20: {'nome_do_livro': 'A Profecia do Eclipse',
         'autor': 'Emma Williams',
         'genero': 'Drama',
         'lancamento': 1996,
         'qtde_disponivel': 23,
         'preço': 99.10},
    21: {'nome_do_livro': 'A Magia Esquecida',
         'autor': 'Sophia Thompson',
         'genero': 'História',
         'lancamento': 1978,
         'qtde_disponivel': 14,
         'preço': 49.50},
    22: {'nome_do_livro': 'O Destino das Estrelas',
         'autor': 'Christopher Wilson',
         'genero': 'Ficção Científica',
         'lancamento': 1987,
         'qtde_disponivel': 0,
         'preço': 66.80},
    23: {'nome_do_livro': 'A Jornada do Viajante',
         'autor': 'Lauren Moore',
         'genero': 'Aventura',
         'lancamento': 2004,
         'qtde_disponivel': 18,
         'preço': 27.90},
    24: {'nome_do_livro': 'O Mistério da Lua Azul',
         'autor': 'Daniel Anderson',
         'genero': 'Mistério',
         'lancamento': 1991,
         'qtde_disponivel': 25,
         'preço': 62.40},
    25: {'nome_do_livro': 'O Desafio do Desconhecido',
         'autor': 'Olivia Jones',
         'genero': 'Thriller',
         'lancamento': 1989,
         'qtde_disponivel': 36,
         'preço': 45.20},
    26: {'nome_do_livro': 'A Conspiração das Sombras',
         'autor': 'Michael Davis',
         'genero': 'Fantasia',
         'lancamento': 2003,
         'qtde_disponivel': 10,
         'preço': 88.70},
    27: {'nome_do_livro': 'A Fronteira do Infinito',
         'autor': 'James Robinson',
         'genero': 'Drama',
         'lancamento': 1980,
         'qtde_disponivel': 16,
         'preço': 53.10},
    28: {'nome_do_livro': 'A Maldição do Abismo',
         'autor': 'Ashley Martinez',
         'genero': 'Mistério',
         'lancamento': 1997,
         'qtde_disponivel': 7,
         'preço': 37.80},
    29: {'nome_do_livro': 'O Legado Perdido',
         'autor': 'Christopher Taylor',
         'genero': 'História',
         'lancamento': 1986,
         'qtde_disponivel': 21,
         'preço': 81.90},
    30: {'nome_do_livro': 'O Labirinto Inexplorado',
         'autor': 'Sarah Williams',
         'genero': 'Ficção Científica',
         'lancamento': 1994,
         'qtde_disponivel': 0,
         'preço': 29.60},
    31: {'nome_do_livro': 'O Segredo do Abismo',
         'autor': 'Jessica White',
         'genero': 'Aventura',
         'lancamento': 2008,
         'qtde_disponivel': 14,
         'preço': 59.80},
    32: {'nome_do_livro': 'O Desafio dos Deuses',
         'autor': 'William Jackson',
         'genero': 'Fantasia',
         'lancamento': 2010,
         'qtde_disponivel': 24,
         'preço': 40.20},
    33: {'nome_do_livro': 'A Última Fronteira',
         'autor': 'Emily Johnson',
         'genero': 'Ficção Científica',
         'lancamento': 2006,
         'qtde_disponivel': 8,
         'preço': 55.30},
    34: {'nome_do_livro': 'O Destino do Universo',
         'autor': 'Christopher Taylor',
         'genero': 'Mistério',
         'lancamento': 2002,
         'qtde_disponivel': 16,
         'preço': 68.90},
    35: {'nome_do_livro': 'O Mistério do Portal',
         'autor': 'Daniel Anderson',
         'genero': 'Drama',
         'lancamento': 2007,
         'qtde_disponivel': 12,
         'preço': 47.60},
    36: {'nome_do_livro': 'A Busca pelo Conhecimento',
         'autor': 'Michael Davis',
         'genero': 'História',
         'lancamento': 2015,
         'qtde_disponivel': 19,
         'preço': 33.40},
    37: {'nome_do_livro': 'O Poder da Magia',
         'autor': 'Lauren Moore',
         'genero': 'Fantasia',
         'lancamento': 2012,
         'qtde_disponivel': 27,
         'preço': 76.20},
    38: {'nome_do_livro': 'A Noite Eterna',
         'autor': 'Brian Miller',
         'genero': 'Mistério',
         'lancamento': 2011,
         'qtde_disponivel': 22,
         'preço': 90.10},
    39: {'nome_do_livro': 'A Queda do Império',
         'autor': 'Sophia Thompson',
         'genero': 'Romance',
         'lancamento': 2009,
         'qtde_disponivel': 9,
         'preço': 25.80},
    40: {'nome_do_livro': 'O Último Guerreiro',
         'autor': 'David Harris',
         'genero': 'Aventura',
         'lancamento': 2018,
         'qtde_disponivel': 35,
         'preço': 43.70},
    41: {'nome_do_livro': 'A Máquina do Tempo',
         'autor': 'William Jackson',
         'genero': 'Ficção Científica',
         'lancamento': 2013,
         'qtde_disponivel': 10,
         'preço': 62.80},
    42: {'nome_do_livro': 'A Revolta dos Robôs',
         'autor': 'Jessica White',
         'genero': 'Thriller',
         'lancamento': 2016,
         'qtde_disponivel': 28,
         'preço': 38.90},
    43: {'nome_do_livro': 'O Despertar da Escuridão',
         'autor': 'Christopher Taylor',
         'genero': 'Fantasia',
         'lancamento': 2014,
         'qtde_disponivel': 17,
         'preço': 49.60},
    44: {'nome_do_livro': 'O Legado do Viajante',
         'autor': 'Lauren Moore',
         'genero': 'Aventura',
         'lancamento': 2019,
         'qtde_disponivel': 23,
         'preço': 56.30},
    45: {'nome_do_livro': 'O Desafio do Tempo',
         'autor': 'Daniel Anderson',
         'genero': 'Mistério',
         'lancamento': 2020,
         'qtde_disponivel': 14,
         'preço': 72.40},
    46: {'nome_do_livro': 'A Conquista da Liberdade',
         'autor': 'Sophia Thompson',
         'genero': 'Drama',
         'lancamento': 2017,
         'qtde_disponivel': 19,
         'preço': 35.20},
    47: {'nome_do_livro': 'O Código do Futuro',
         'autor': 'Brian Miller',
         'genero': 'Ficção Científica',
         'lancamento': 2022,
         'qtde_disponivel': 8,
         'preço': 90.60},
    48: {'nome_do_livro': 'A Batalha Interdimensional',
         'autor': 'Michael Davis',
         'genero': 'Aventura',
         'lancamento': 2021,
         'qtde_disponivel': 25,
         'preço': 42.30},
    49: {'nome_do_livro': 'O Segredo das Estrelas',
         'autor': 'Emma Martin',
         'genero': 'Fantasia',
         'lancamento': 2023,
         'qtde_disponivel': 12,
         'preço': 53.70},
    50: {'nome_do_livro': 'A Última Fronteira',
         'autor': 'Christopher Wilson',
         'genero': 'Mistério',
         'lancamento': 2002,
         'qtde_disponivel': 16,
         'preço': 68.90}

}

while True:

    imprimir_menu()

    try:

        opcao_escolhida = int(input("\nOpção escolhida: "))

        if opcao_escolhida not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            continue

        if opcao_escolhida == 1:

            while True:

                print("\nMODO >>ADICIONAR NOVO CLIENTE<<")

                numero_cpf = solicitar_cpf_cliente()

                if numero_cpf == '000':
                    print()
                    break

                if numero_cpf not in dicionario_cpf_nomecliente_valorcompras_segmento:
                    nome = solicitar_nome_cliente()
                    email = solicitar_email_cliente()
                    telefone = solicitar_telefone_cliente()
                    valor_total_compras = 0
                    livros_comprados = {}
                    segmento = atribuir_segmento(valor_total_compras)
                    dicionario_cpf_nomecliente_valorcompras_segmento[numero_cpf] = {'nome': nome,
                                                                                    'email': email,
                                                                                    'telefone': telefone,
                                                                                    'valor_total_compras': valor_total_compras,
                                                                                    'segmento': segmento,
                                                                                    'livros_comprados': livros_comprados}
                    print(f"\nCliente {nome} (CPF: {numero_cpf[:3]}.{numero_cpf[3:6]}.{numero_cpf[6:9]}-{numero_cpf[9:]}) adicionado com sucesso!\n")
                    break

                elif numero_cpf in dicionario_cpf_nomecliente_valorcompras_segmento:
                    print(f"\nCPF já existente no cadastro."
                          f"\nNome: {dicionario_cpf_nomecliente_valorcompras_segmento[numero_cpf]['nome']}"
                          "\nDeseja adicionar valor de compras a este CPF?")

        elif opcao_escolhida == 2:

            while True:

                print("\nMODO >>REMOVER CLIENTE<<\n")

                numero_cpf = solicitar_cpf_cliente()

                if numero_cpf == '000':
                    break

                while numero_cpf not in dicionario_cpf_nomecliente_valorcompras_segmento:
                    print("CPF não cadastrado na base de dados!")
                    numero_cpf = solicitar_cpf_cliente()
                    if numero_cpf == '000':
                        break

                if numero_cpf in dicionario_cpf_nomecliente_valorcompras_segmento:
                    remover_cliente(numero_cpf, dicionario_cpf_nomecliente_valorcompras_segmento)
                    print("Deseja remover mais algum cliente do sistema?\n\n"
                          "  [1] SIM\n"
                          "  [2] NÃO\n")

                    continuar = int(input("Opção desejada: "))

                    while continuar not in [1, 2]:
                        print("Digite uma opção válida!\n\n"
                              "Deseja remover mais algum cliente do sistema?\n\n"
                              "  [1] SIM\n"
                              "  [2] NÃO\n")

                    if continuar == 1:
                        continue

                    if continuar == 2:
                        break

        elif opcao_escolhida == 3:

            while True:

                print("\nMODO >>ALTERAR DADOS DE UM CLIENTE<<\n")

                numero_cpf = solicitar_cpf_cliente()

                if numero_cpf == '000':
                    break

                while numero_cpf not in dicionario_cpf_nomecliente_valorcompras_segmento:
                    print("CPF não cadastrado na base de dados!")
                    numero_cpf = solicitar_cpf_cliente()
                    if numero_cpf == '000':
                        break

                if numero_cpf in dicionario_cpf_nomecliente_valorcompras_segmento:
                    alterar_dados_cliente(numero_cpf, dicionario_cpf_nomecliente_valorcompras_segmento)

        elif opcao_escolhida == 4:

            print("\nMODO >>CONSULTAR BASE DE CLIENTES<<\n")

            if dicionario_cpf_nomecliente_valorcompras_segmento == {}:
                print("Ainda não há nenhum cliente cadastrado.")
                print()

            else:
                ver_base_de_dados_clientes(dicionario_cpf_nomecliente_valorcompras_segmento)

        elif opcao_escolhida == 5:

            while True:

                print("\nMODO >>REGISTRAR COMPRA<<")

                numero_cpf = solicitar_cpf_cliente()

                if numero_cpf == '000':
                    break

                if numero_cpf not in dicionario_cpf_nomecliente_valorcompras_segmento and numero_cpf != 000:

                    print("\nCPF não cadastrado na base de dados!\n")

                    cadastrar_cliente = input("Deseja cadastrar cliente agora? [S/N]").strip().upper()

                    if cadastrar_cliente == 'S':
                        while True:

                            print("\nMODO >>ADICIONAR NOVO CLIENTE<<\n")

                            numero_cpf_cadastro = solicitar_cpf_cliente()

                            if numero_cpf_cadastro == '000':
                                print("Operação cancelada.")
                                break


                            else:
                                nome = solicitar_nome_cliente()
                                email = solicitar_email_cliente()
                                telefone = solicitar_telefone_cliente()
                                valor_total_compras = 0
                                livros_comprados = {}
                                segmento = atribuir_segmento(valor_total_compras)
                                dicionario_cpf_nomecliente_valorcompras_segmento[numero_cpf] = {'nome': nome,
                                                                                                'email': email,
                                                                                                'telefone': telefone,
                                                                                                'valor_total_compras': valor_total_compras,
                                                                                                'segmento': segmento,
                                                                                                'livros_comprados': livros_comprados}

                                break
                        break

                    elif cadastrar_cliente == 'N':
                        break

                    else:
                        continue

                if numero_cpf in dicionario_cpf_nomecliente_valorcompras_segmento:
                    print(f"\nCPF encontrado no sistema!\n\n"
                          f"(CPF: {numero_cpf[:3]}.{numero_cpf[3:6]}.{numero_cpf[6:9]}-{numero_cpf[9:]})\n"
                          f"Nome: {dicionario_cpf_nomecliente_valorcompras_segmento[numero_cpf]['nome']}")
                    registrar_compra(numero_cpf, dicionario_cpf_nomecliente_valorcompras_segmento, dicionario_livros)
                    print()
                    break


        elif opcao_escolhida == 6:

            print("\nMODO >>ADICIONAR LIVRO AO SISTEMA<<")

            while True:

                adicionar_livro(dicionario_livros)

                continuar_adicionando = input("Deseja continuar adicionando algum livro ao sistema? [S/N]: ").upper().strip().rstrip().lstrip()

                if continuar_adicionando == 'S':
                    continue

                else:
                    print()
                    break

        elif opcao_escolhida == 7:


            alterar_dados_livro(dicionario_livros)


        elif opcao_escolhida == 8:

            while True:

                remover_livro(dicionario_livros)

                continuar_removendo = input("Deseja remover mais algum livro? [S/N]: ").upper().strip()

                if continuar_removendo == 'S':
                    continue

                else:
                    break


        elif opcao_escolhida == 9:

            while True:

                print("\nDeseja buscar o livro por palavra-chave, gênero, ou autor?\n\n"
                                    "  [1] Palavra-chave\n"
                                    "  [2] Gênero\n"
                                    "  [3] Autor")

                opcao_busca = input("\nOpção escolhida ('000' para sair): ")

                if opcao_busca == '1':

                    palavra_chave_digitada = input("\nDigite a palavra-chave/parte do nome do livro:").strip()

                    resultado = buscar_livros(dicionario_livros, palavra_chave=palavra_chave_digitada)

                    print()

                    for livro_id, livro_info in resultado:

                        print(f"ID: {livro_id}\n"
                              f"Nome: {livro_info['nome_do_livro']}\n"
                              f"Autor: {livro_info['autor']}\n"
                              f"Gênero: {livro_info['genero']}\n"
                              f"Lançamento: {livro_info['lancamento']}\n"
                              f"Qtde disponível: {livro_info['qtde_disponivel']}\n"
                              f"Preço: R${livro_info['preço']:,.2f}\n"
                              f"----------------------------------")

                elif opcao_busca == '2':

                    genero_digitado = input("\nDigite o gênero: ").strip()

                    resultado = buscar_livros(dicionario_livros, genero=genero_digitado)

                    print()

                    for livro_id, livro_info in resultado:

                        print(f"ID: {livro_id}\n"
                              f"Nome: {livro_info['nome_do_livro']}\n"
                              f"Autor: {livro_info['autor']}\n"
                              f"Gênero: {livro_info['genero']}\n"
                              f"Lançamento: {livro_info['lancamento']}\n"
                              f"Qtde disponível: {livro_info['qtde_disponivel']}\n"
                              f"Preço: R${livro_info['preço']:,.2f}\n"
                              f"----------------------------------")

                elif opcao_busca == '3':

                    autor_digitado = input("\nDigite o nome do autor: ").strip()

                    resultado = buscar_livros(dicionario_livros, autor=autor_digitado)

                    print()

                    for livro_id, livro_info in resultado:

                        print(f"ID: {livro_id}\n"
                              f"Nome: {livro_info['nome_do_livro']}\n"
                              f"Autor: {livro_info['autor']}\n"
                              f"Gênero: {livro_info['genero']}\n"
                              f"Lançamento: {livro_info['lancamento']}\n"
                              f"Qtde disponível: {livro_info['qtde_disponivel']}\n"
                              f"Preço: R${livro_info['preço']:,.2f}\n"
                              f"----------------------------------")
                elif opcao_busca == '000':
                    print()
                    break
                else:
                    continue


    except ValueError:

        print("\nDigite apenas o número referente a opção válida.\n")

        continue

## FIM DO CÓDIGO