from pydantic import BaseModel

class Tarefa(BaseModel):
    id:int
    titulo:str
    descricao:str
    concluido:bool
    