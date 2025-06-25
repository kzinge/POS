import requests

def listar_livros(url):
    r = requests.get(f"{url}/livros")
    livros = r.json()

    if not livros:
        print("Nenhum livro foi cadastrado ainda")
    else:
        print('Lista de Livros:')
        for livro in livros:
            print(f"- Título: {livro['titulo']}, Ano: {livro['ano']}, Edição: {livro['edicao']}")


def pesquisar_livro_titulo(url):
    titulo = input("Digite o título do livro: ").title()
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code == 404:
        print("Nenhum livro foi encontrado")
    elif r.status_code == 200:
        print("Livro Encontrado:")
        livro = r.json()
        print(f"- Título: {livro['titulo']}, Ano: {livro['ano']}, Edição: {livro['edicao']}")

        return livro

def cadastrar_livro(url):
    print("Opa! Vamos Cadastrar mais um livro!")
    titulo = input("Digite o título do livro: ").title()
    ano = int(input(f"Digite o ano de publicação de {titulo}: "))
    edicao = int(input(f"Digite a edição de {titulo}: "))
    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }

    print(f"""Prévia do Livro:\n
    Título: {titulo}
    Ano: {ano}
    Edição: {edicao}
    """)
    confirmacao = input("Deseja salvar o livro? (S/N)").upper()

    if confirmacao == "S":
        r = requests.post(f"{url}/livros", json=livro)
        if r.status_code == 200 or r.status_code ==201:
            print("Livro cadastrado com sucesso!")
        else:
            print(f"Erro ao cadastrar: {r.status_code}")
            print(r.text)

    else:
        print("Cadastro cancelado pelo usuário.")

def deletar_livro(url):
    listar_livros(url)
    print('\n')
    titulo = input("Digite o titulo do livro que será deletado: ").title()
    r = requests.delete(f"{url}/livros/{titulo}")

    if r.status_code == 200:
        print("Livro deletado com sucesso!")
    else:
        print("Erro ao deletar livro, verifique se o titulo está correto.")

def editar_livro(url):
    listar_livros(url)
    print('\n')
    livro = pesquisar_livro_titulo(url)
    titulo = livro['titulo']
    print('\n')
    print(f'== Edição de {titulo} ==')

    print("Escolha o que você deseja editar:")
    print("1 - Só o título")
    print("2 - Só o ano")
    print("3 - Só a edição")
    print("4 - Só o titulo e ano")
    print("5 - Só o titulo e edição")
    print("6 - Só o edição e ano")

    opcao_de_edicao = input("Digite a sua escolha: ")

    if opcao_de_edicao == "1":
        novo_titulo = input(f"Altere o título: {titulo} para: ")
        novo_ano = livro['ano']
        nova_edicao = livro['edicao']

        novo_livro = {
            "titulo": novo_titulo,
            "ano": novo_ano,
            "edicao": nova_edicao
        }

        r = requests.put(f"{url}/livros/{titulo}", json=novo_livro)
        if r.status_code == 200:
            print("Livro Atualizado com Sucesso!")
        else:
            print("Erro ao atualizar livro")

    elif opcao_de_edicao == "2":
        novo_titulo = titulo
        novo_ano = int(input(f"Altere o ano: {livro['ano']} para: "))
        nova_edicao = livro['edicao']

        novo_livro = {
            "titulo": novo_titulo,
            "ano": novo_ano,
            "edicao": nova_edicao
        }

        r = requests.put(f"{url}/livros/{titulo}", json=novo_livro)
        if r.status_code == 200:
            print("Livro Atualizado com Sucesso!")
        else:
            print("Erro ao atualizar livro")

    elif opcao_de_edicao == "3":
        novo_titulo = titulo
        novo_ano = livro['ano']
        nova_edicao = int(input(f"Altere a edição: {livro['edicao']} para: "))

        novo_livro = {
            "titulo": novo_titulo,
            "ano": novo_ano,
            "edicao": nova_edicao
        }

        r = requests.put(f"{url}/livros/{titulo}", json=novo_livro)
        if r.status_code == 200:
            print("Livro Atualizado com Sucesso!")
        else:
            print("Erro ao atualizar livro")

    elif opcao_de_edicao == "4":
        novo_titulo = input(f"Altere o título: {titulo} para: ")
        novo_ano = int(input(f"Altere o ano: {livro['ano']} para: "))
        nova_edicao = livro['edicao']

        novo_livro = {
            "titulo": novo_titulo,
            "ano": novo_ano,
            "edicao": nova_edicao
        }

        r = requests.put(f"{url}/livros/{titulo}", json=novo_livro)
        if r.status_code == 200:
            print("Livro Atualizado com Sucesso!")
        else:
            print("Erro ao atualizar livro")

    elif opcao_de_edicao == "5":
        novo_titulo = input(f"Altere o título: {titulo} para: ")
        novo_ano = livro['ano']
        nova_edicao = int(input(f"Altere a edição: {livro['edicao']} para: "))

        novo_livro = {
            "titulo": novo_titulo,
            "ano": novo_ano,
            "edicao": nova_edicao
        }

        r = requests.put(f"{url}/livros/{titulo}", json=novo_livro)
        if r.status_code == 200:
            print("Livro Atualizado com Sucesso!")
        else:
            print("Erro ao atualizar livro")

    elif opcao_de_edicao == "6":
        novo_titulo = titulo
        novo_ano = int(input(f"Altere o ano: {livro['ano']} para: "))
        nova_edicao = int(input(f"Altere a edição: {livro['edicao']} para: "))

        novo_livro = {
            "titulo": novo_titulo,
            "ano": novo_ano,
            "edicao": nova_edicao
        }

        r = requests.put(f"{url}/livros/{titulo}", json=novo_livro)
        if r.status_code == 200:
            print("Livro Atualizado com Sucesso!")
        else:
            print("Erro ao atualizar livro")

    else:
        print("Opção inválida. Nenhuma alteração foi feita.")

