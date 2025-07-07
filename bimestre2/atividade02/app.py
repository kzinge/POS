from functions import *

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"
    
    while True:
        print("\n=== MENU DE CARROS ===")
        print("1 - Listar todos os carros")
        print("2 - Pesquisar carro por placa")
        print("3 - Cadastrar um carro")
        print("4 - Deletar um carro")
        print("5 - Editar um carro")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_carros(url)
        elif opcao == "2":
            pesquisar_carro_placa(url)
        elif opcao == "3":
            cadastrar_carro(url)
        elif opcao == "4":
            deletar_carro(url)
        elif opcao == "5":
            editar_carro(url)
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
