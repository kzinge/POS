import requests

def listar_carros(url):
    r = requests.get(f"{url}/carros")
    carros = r.json()

    if not carros:
        print("Nenhum carro foi cadastrado ainda.")
    else:
        print('Lista de Carros:')
        for carro in carros:
            print(f"- Placa: {carro['placa']}, Nome: {carro['nome']}, Marca: {carro['marca']}, Modelo: {carro['modelo']}")

def pesquisar_carro_placa(url):
    placa = input("Digite a placa do carro: ").upper()
    r = requests.get(f"{url}/carros/{placa}")
    if r.status_code == 404:
        print("Nenhum carro foi encontrado.")
    elif r.status_code == 200:
        print("Carro Encontrado:")
        carro = r.json()
        print(f"- Placa: {carro['placa']}, Nome: {carro['nome']}, Marca: {carro['marca']}, Modelo: {carro['modelo']}")
        return carro

def cadastrar_carro(url):
    print("Vamos cadastrar um novo carro:")
    placa = input("Digite a placa do carro: ").upper()
    nome = input("Digite o nome do carro: ").title()
    marca = input(f"Digite a marca de {nome}: ").title()
    modelo = input(f"Digite o modelo de {nome}: ").title()

    carro = {
        "placa": placa,
        "nome": nome,
        "marca": marca,
        "modelo": modelo
    }

    print(f"""\nPrévia do Carro:
    Placa: {placa}
    Nome: {nome}
    Marca: {marca}
    Modelo: {modelo}
    """)

    confirmacao = input("Deseja salvar o carro? (S/N): ").upper()
    if confirmacao == "S":
        r = requests.post(f"{url}/carros", json=carro)
        if r.status_code in [200, 201]:
            print("Carro cadastrado com sucesso!")
        else:
            print(f"Erro ao cadastrar: {r.status_code}")
            print(r.text)
    else:
        print("Cadastro cancelado pelo usuário.")

def deletar_carro(url):
    listar_carros(url)
    print('\n')
    placa = input("Digite a placa do carro que será deletado: ").upper()
    r = requests.delete(f"{url}/carros/{placa}")

    if r.status_code == 200:
        print("Carro deletado com sucesso!")
    else:
        print("Erro ao deletar carro. Verifique se a placa está correta.")

def editar_carro(url):
    listar_carros(url)
    print('\n')
    carro = pesquisar_carro_placa(url)
    placa = carro['placa']
    print('\n== Edição do carro com placa:', placa, '==')

    print("Escolha o que você deseja editar:")
    print("1 - Só o nome")
    print("2 - Só a marca")
    print("3 - Só o modelo")
    print("4 - Nome e marca")
    print("5 - Nome e modelo")
    print("6 - Modelo e marca")

    opcao = input("Digite a sua escolha: ")

    novo_nome = carro['nome']
    nova_marca = carro['marca']
    novo_modelo = carro['modelo']

    if opcao == "1":
        novo_nome = input(f"Novo nome (atual: {carro['nome']}): ").title()
    elif opcao == "2":
        nova_marca = input(f"Nova marca (atual: {carro['marca']}): ").title()
    elif opcao == "3":
        novo_modelo = input(f"Novo modelo (atual: {carro['modelo']}): ").title()
    elif opcao == "4":
        novo_nome = input(f"Novo nome (atual: {carro['nome']}): ").title()
        nova_marca = input(f"Nova marca (atual: {carro['marca']}): ").title()
    elif opcao == "5":
        novo_nome = input(f"Novo nome (atual: {carro['nome']}): ").title()
        novo_modelo = input(f"Novo modelo (atual: {carro['modelo']}): ").title()
    elif opcao == "6":
        nova_marca = input(f"Nova marca (atual: {carro['marca']}): ").title()
        novo_modelo = input(f"Novo modelo (atual: {carro['modelo']}): ").title()
    else:
        print("Opção inválida. Nenhuma alteração foi feita.")
        return

    novo_carro = {
        "placa": placa,
        "nome": novo_nome,
        "marca": nova_marca,
        "modelo": novo_modelo
    }

    r = requests.put(f"{url}/carros/{placa}", json=novo_carro)
    if r.status_code == 200:
        print("Carro atualizado com sucesso!")
    else:
        print("Erro ao atualizar carro.")
