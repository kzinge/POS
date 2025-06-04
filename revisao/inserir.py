import requests

BASE_URL = "http://127.0.0.1:8000/livros/"

livros_para_inserir = [
    {
        "id": 1,
        "titulo": "1984",
        "autor": "George Orwell",
        "ano_publicacao": "1949",
        "disponivel": True
    },
    {
        "id": 2,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano_publicacao": "1899",
        "disponivel": False
    },
    {
        "id": 3,
        "titulo": "A Revolução dos Bichos",
        "autor": "George Orwell",
        "ano_publicacao": "1945",
        "disponivel": True
    },
    {
        "id": 4,
        "titulo": "Capitães da Areia",
        "autor": "Jorge Amado",
        "ano_publicacao": "1937",
        "disponivel": True
    },
    {
        "id": 5,
        "titulo": "Memórias Póstumas de Brás Cubas",
        "autor": "Machado de Assis",
        "ano_publicacao": "1881",
        "disponivel": True
    }
]

for livro in livros_para_inserir:
    response = requests.post(BASE_URL, json=livro)
    if response.status_code == 200:
        print(f"Livro Adicionado! {livro['titulo']}")
    else:
        print(f"Erro ao inserir livro {livro['titulo']} : {response.status_code} - {response.text}")