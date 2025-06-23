import requests

if __name__ == '__main__':
    url = "http://localhost:8000"
    r = requests.get(f"{url}/livros")
    print(r.text)

    livro = {
        "titulo":"teste2322 com requests",
        "ano": 2025,
        "edicao": 1
    }

    novo_livro = requests.post(f"{url}/livros", json=livro)
    print(novo_livro.status_code)
    print(novo_livro.text)

    pesquisa = 'teste com requests'
    filtro = requests.get(f"{url}/livros/{pesquisa}")
    print(filtro.status_code)
    print(filtro.text)

    livro_del = 'teste232 com requests'
    delete = requests.delete(f"{url}/livros/{livro_del}")
    print(delete.status_code)