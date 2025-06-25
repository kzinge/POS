from fastapi import FastAPI, HTTPException
from model import *
from typing import List

app = FastAPI()


usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

#Usuário
@app.get("/usuarios/", response_model=list[Usuario])
def listar_usuarios():
    return usuarios

#Cadastrar usuário
@app.post("/usuarios/", response_model=Usuario)
def cadastrar_usuario(user: Usuario):
    user.data_criacao = datetime.now()
    usuarios.append(user)
    return user

@app.delete("/usuarios/{user_name}", response_model=Usuario)
def deletar_usuario(user_name: str):
    for index, user in enumerate(usuarios):
        if user.username == user_name:
            del usuarios[index]
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

#-----------------------------------------------------------------------------

#Livro
@app.get("/livros/", response_model=list[Livro])
def listar_livros():
    return livros

#Cadastrar usuário
@app.post("/livros/", response_model=Livro)
def cadastrar_livro(livro: Livro):
    livros.append(livro)
    return livro

@app.delete("/livros/{livro_titulo}", response_model=Livro)
def deletar_livro(livro_titulo: str):
    for index, livro in enumerate(livros):
        if livro.username == livro_titulo:
            del livros[index]
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

#----------------------------------------------------------------------------

#Biblioteca
@app.get("/bibliotecas/", response_model=list[Biblioteca])
def listar_bibs():
    return bibliotecas

#Cadastrar bib
@app.post("/bibliotecas/", response_model=Biblioteca)
def cadastrar_bib(bib: Biblioteca):
    bibliotecas.append(bib)
    return bib

@app.delete("/bibliotecas/{bib_nome}", response_model=Biblioteca)
def deletar_bib(bib_nome: str):
    for index, bib in enumerate(livros):
        if bib.nome == bib_nome:
            del bibliotecas[index]
            return bib
    raise HTTPException(status_code=404, detail="Biblioteca não encontrada")

#-----------------------------------------------------------------------------

#Emprestimo
@app.get("/emprestimos/", response_model=list[Emprestimo])
def listar_emps():
    return emprestimos


@app.post("/emprestimos/", response_model=Emprestimo)
def cadastrar_bib(emp: Emprestimo):
    emp.data_emprestimo = datetime.date()
    emprestimos.append(emp)
    return emp

@app.delete("/emprestimos/{user_name}", response_model=Biblioteca)
def deletar_bib(user_name: str):
    for index, emp in enumerate(usuarios):
        if emp.usuario.username == user_name:
            del emprestimos[index]
            return emp
    raise HTTPException(status_code=404, detail="Emprestimo não encontrado")
