from fastapi import FastAPI, HTTPException
from models import Tarefa
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

#Salva tarefas na memória, sem banco
tarefas: List[Tarefa] = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Listar
@app.get("/tarefas/", response_model=list[Tarefa])
def listar_tarefas():
    return tarefas

#Cadastrar tarefas
@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    tarefa.id = len(tarefas) + 1
    tarefas.append(tarefa)
    return tarefa

@app.delete("/tarefas/", response_model=Tarefa)
def deletar_tarefa(tarefa_id:int):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[index]
            return tarefa
        raise HTTPException(status_code=404, detail="Não Localizado")
