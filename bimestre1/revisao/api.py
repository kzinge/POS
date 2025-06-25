from fastapi import FastAPI, HTTPException  # Importa a classe principal do FastAPI e a exceção HTTP para erros personalizados
from models import Livros                   # Importa o modelo de dados Livros, que representa a estrutura dos livros
from typing import List                     # Importa o tipo List para tipagem de listas

app = FastAPI()  # Inicializa a aplicação FastAPI

# Lista que simula um banco de dados temporário em memória
livros: List[Livros] = []

# Rota POST para criar um novo livro
@app.post("/livros/", response_model=Livros)  # Define a rota POST que retorna o modelo Livros
def create_livro(livro: Livros):              # Função que recebe um livro como entrada
    livros.append(livro)                      # Adiciona o livro à lista (simulando salvar no "banco")
    return livro                              # Retorna o livro criado

# Rota GET para retornar todos os livros cadastrados
@app.get("/livros/", response_model=List[Livros])  # Rota GET que retorna uma lista de livros
def read_livros():
    return livros  # Retorna todos os livros

# Rota GET para retornar um livro específico pelo ID
@app.get("/livros/{id}", response_model=Livros)  # O {id} indica um parâmetro dinâmico na rota
def read_livro(id: int):                         # A função recebe o ID como inteiro
    for index, livro in enumerate(livros):       # Percorre a lista de livros
        if livro.id == id:                       # Verifica se o ID bate com o livro atual
            return livro                         # Retorna o livro encontrado
    raise HTTPException(status_code=404, detail="Livro não encontrado")  # Se não encontrar, retorna erro 404

# Rota PUT para atualizar um livro pelo ID
@app.put("/livros/{id}", response_model=Livros)  # Rota PUT usada para atualizar um livro
def update_livro(id: int, livro_atualizado: Livros):  # Recebe o ID e os dados atualizados
    for index, livro in enumerate(livros):            # Percorre os livros
        if livro.id == id:                            # Se encontrar o livro com o ID correspondente
            livro_atualizado.id = id                  # Garante que o ID permaneça o mesmo
            livros[index] = livro_atualizado          # Substitui o livro antigo pelo novo
            return livro_atualizado                   # Retorna o livro atualizado
    raise HTTPException(status_code=404, detail="Livro não encontrado")  # Se não encontrar, retorna erro 404

# Rota DELETE para remover um livro pelo ID
@app.delete("/livros/{id}", response_model=Livros)  # Rota DELETE usada para remover um livro
def delete_livro(id: int):
    for index, livro in enumerate(livros):         # Percorre os livros
        if livro.id == id:                         # Se encontrar o ID
            del livros[index]                      # Remove o livro da lista
            return livro                           # Retorna o livro removido
    raise HTTPException(status_code=404, detail="Livro não encontrado")  # Caso não encontre, erro 404

# Rota GET para buscar livros por autor
@app.get("/livros/autor/{autor}", response_model=List[Livros])  # Rota para buscar livros de um autor específico
def find_livros(autor: str):                                    # Recebe o nome do autor como parâmetro
    encontrados = [livro for livro in livros if livro.autor == autor]  # Filtra os livros que têm o autor correspondente
    if encontrados:                                             # Se encontrar algum
        return encontrados                                      # Retorna a lista de livros do autor
    else:
        raise HTTPException(status_code=404, detail="Nenhum livro correspondente ao autor foi encontrado")  # Erro 404 se não encontrar
