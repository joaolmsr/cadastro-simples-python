lista_de_filmes = []
lista_de_clientes = []

while True:
  menu = input("""
  Escolha uma opção:
  1 - Filmes
  2 - Clientes
  0 - Sair
""")
  match menu: #esse aqui é o do menu principal onde só da pra entrar no menu dos filmes ou dos clientes ou fechar o programa
    case "1":
      while True:
        menu_dos_filmes = input("""
        Escolha uma opção:
        1 - Cadastrar Filme
        2 - Ver todos os filmes cadastrados
        3 - Editar filme cadastrado
        4 - Excluir filme cadastrado
        5 - Alugar um filme
        0 - Voltar ao Menu Principal
        """)
        match menu_dos_filmes:
          case "1":
            titulo = input("Digite o titulo do filme: ")
            genero = input("Digite o genero do filme: ")
            preco = float(input("Digite o preço do filme: "))

            novo_filme = {
              "Título": titulo,
              "Gênero": genero,
              "Preço": preco,
              "Status": True
            }
            lista_de_filmes.append(novo_filme)
            print("Filme Cadastrado com sucesso")

          case "2":
            if len(lista_de_filmes) == 0:
              print("Lista Vazia, nenhum filme cadastrado")
            else:
              for filme_da_vez in lista_de_filmes:
                print(f"""
                Título do filme: {filme_da_vez["Título"]}
                Gênero do filme: {filme_da_vez["Gênero"]}
                Preço de aluguel do filme: R${filme_da_vez["Preço"]}
                Disponibilidade do filme: {filme_da_vez["Status"]}
                """)
          case "3":
              for filme_da_vez in lista_de_filmes: # isso aqui é uma previsualização para que o usuário saiba quais são os filmes que existem antes de escolher qual ele quer deletar.
                print(f"""
                Título do filme: {filme_da_vez["Título"]}
                """)
              filme_escolhido_para_editar = input("Digite o título do filme que você quer editar: ")
              
              encontrei_o_filme = False

              for filme_em_questao in lista_de_filmes:
                if filme_em_questao["Título"] == filme_escolhido_para_editar:
                  menu_de_editar_filme = input("""
                  Qual o atributo que você quer editar:
                  1 - Título do filme
                  2 - Gênero do filme
                  3 - Preço do filme
                  0 - Voltar
                  """)
                  match menu_de_editar_filme:
                    case "1":
                      novo_titulo = input("Digite o novo título do filme: ")
                      filme_em_questao["Título"] = novo_titulo
                    case "2":
                      novo_genero = input("Digite o novo gênero do filme: ")
                      filme_em_questao["Gênero"] = novo_genero
                    case "3":
                      novo_preco = input("Digite o novo preço do filme: ")
                      filme_em_questao["Preço"] = novo_preco
                    case "0":
                      break
                    case _:
                      print("Opção Inválida")
                  encontrei_o_filme = True
                  print("Filme deletado com sucesso")
              if encontrei_o_filme == False:
                print("Filme não encontrado")


          case "4":
              for filme_da_vez in lista_de_filmes: # isso aqui é uma previsualização para que o usuário saiba quais são os filmes que existem antes de escolher qual ele quer deletar.
                print(f"""
                Título do filme: {filme_da_vez["Título"]}
                """)
              filme_escolhido_para_deletar = input("Digite o título do filme que você quer deletar: ")

              encontrei_o_filme = False
              for filme_em_questao in lista_de_filmes:
                if filme_em_questao["Título"] == filme_escolhido_para_deletar:
                  lista_de_filmes.remove(filme_em_questao)
                  encontrei_o_filme = True
                  print("Filme deletado com sucesso")
              if encontrei_o_filme == False:
                print("Filme não encontrado")
          case "5":
            nome_do_cliente = input("Digite o nome do cliente: ")
            for cliente_da_vez in lista_de_clientes:
              if cliente_da_vez["Nome"] == nome_do_cliente:
                nome_do_filme = input("Digite o nome do filme: ")
                encontrei_o_filme = False
                for filme_da_vez in lista_de_filmes:
                  if filme_da_vez["Título"] == nome_do_filme:
                    encontrei_o_filme = True
                    if filme_da_vez["Status"] == False:
                      filme_da_vez["Status"] = True
                      cliente_da_vez["Filmes_em_posse"].append(filme_da_vez)
                      print(f"O Filme {filme_da_vez["Título"]} foi alugado para o cliente {cliente_da_vez["Nome"]}")
                if encontrei_o_filme == False:
                  print("Filme não encontrado")
          case "0":
            break
          case _:
            print("Opção inválida")
    case "2":
      while True:
        menu_dos_clientes = input("""
        Escolha uma opção:
        1 - Cadastrar cliente
        2 - Ver todos os clientes cadastrados
        3 - Editar cliente cadastrado
        4 - Excluir cliente cadastrado
        0 - Voltar ao Menu Principal
        """)
        match menu_dos_clientes:
          case "1":
            nome = input("Digite o nome do cliente: ")
            idade = int(input("Digite o idade do cliente: "))
            telefone = input("Digite o telefone do cliente: ")

            novo_cliente = {
              "Nome": nome,
              "Idade": idade,
              "Telefone": telefone,
              "Filmes_em_posse": []
            }
            lista_de_clientes.append(novo_cliente)
            print("Cliente Cadastrado com sucesso")

          case "2":
            if len(lista_de_clientes) == 0:
              print("Lista Vazia, nenhum cliente cadastrado")
            else:
              for cliente_da_vez in lista_de_clientes:
                print(f"""
                Nome do cliente: {cliente_da_vez["Nome"]}
                Idade do cliente: {cliente_da_vez["Idade"]}
                Telefone do cliente:{cliente_da_vez["Telefone"]}
                """)
          case "3":
              for cliente_da_vez in lista_de_clientes: # isso aqui é uma previsualização para que o usuário saiba quais são os clientes que existem antes de escolher qual ele quer deletar.
                print(f"""
                Nome do cliente: {cliente_da_vez["Nome"]}
                """)
              cliente_escolhido_para_editar = input("Digite o Nome do cliente que você quer editar: ")
              
              encontrei_o_cliente = False

              for cliente_em_questao in lista_de_clientes:
                if cliente_em_questao["Nome"] == cliente_escolhido_para_editar:
                  menu_de_editar_cliente = input("""
                  Qual o atributo que você quer editar:
                  1 - Nome do cliente
                  2 - Idade do cliente
                  3 - Telefone do cliente
                  0 - Voltar
                  """)
                  match menu_de_editar_cliente:
                    case "1":
                      novo_nome = input("Digite o novo Nome do cliente: ")
                      cliente_em_questao["Nome"] = novo_nome
                    case "2":
                      nova_idade = input("Digite o novo Idade do cliente: ")
                      cliente_em_questao["Idade"] = nova_idade
                    case "3":
                      novo_telefone = input("Digite o novo Telefone do cliente: ")
                      cliente_em_questao["Telefone"] = novo_telefone
                    case "0":
                      break
                    case _:
                      print("Opção Inválida")
                  encontrei_o_cliente = True
                  print("cliente deletado com sucesso")
              if encontrei_o_cliente == False:
                print("cliente não encontrado")


          case "4":
              for cliente_da_vez in lista_de_clientes: # isso aqui é uma previsualização para que o usuário saiba quais são os clientes que existem antes de escolher qual ele quer deletar.
                print(f"""
                Nome do cliente: {cliente_da_vez["Nome"]}
                """)
              cliente_escolhido_para_deletar = input("Digite o nome do cliente que você quer deletar: ")

              encontrei_o_cliente = False
              for cliente_em_questao in lista_de_clientes:
                if cliente_em_questao["Nome"] == cliente_escolhido_para_deletar:
                  lista_de_clientes.remove(cliente_em_questao)
                  encontrei_o_cliente = True
                  print("cliente deletado com sucesso")
              if encontrei_o_cliente == False:
                print("cliente não encontrado")
          case "0":
            break
          case _:
            print("Opção inválida")
    case "0":
      break
    case _: #isso aqui é o equivalente ao else
      print("Opção Inválida")