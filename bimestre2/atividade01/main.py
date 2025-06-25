from functions import *

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"
    
    while True:
        print("\n=== MENU ===")
        print("1 - Listar todos os livros")
        print("2 - Pesquisar livro por título")
        print("3 - Cadastrar um livro")
        print("4 - Deletar um livro")
        print("5 - Editar um livro")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros(url)
        elif opcao == "2":
            pesquisar_livro_titulo(url)
        elif opcao == "3":
            cadastrar_livro(url)
        elif opcao == "4":
            deletar_livro(url)
        elif opcao == "5":
            editar_livro(url)
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    
