from fastapi import FastAPI,HTTPException
from models import Carro
from typing import List
app = FastAPI()
carros:List[Carro]=[]


# Create
@app.post("/carros", response_model=Carro)
def criar_carro(carro: Carro):
    for c in carros:
        if c.placa == carro.placa:
            raise HTTPException(status_code=400, detail="Placa já cadastrada.")
    carros.append(carro)
    return carro

@app.get("/carros", response_model=List[Carro])
def listar_carros():
    return carros
@app.get("/carros/{placa}", response_model=Carro)
def buscar_carro(placa: str):
    for c in carros:
        if c.placa == placa:
            return c
    raise HTTPException(status_code=404, detail="Carro não encontrado.")

@app.put("/carros/{placa}", response_model=Carro)
def atualizar_carro(placa: str, dados: Carro):
    for i, c in enumerate(carros):
        if c.placa == placa:
            carros[i] = dados
            return dados
    raise HTTPException(status_code=404, detail="Carro não encontrado.")

@app.delete("/carros/{placa}")
def deletar_carro(placa: str):
    for i, c in enumerate(carros):
        if c.placa == placa:
            del carros[i]
            return {"mensagem": "Carro removido com sucesso"}
    raise HTTPException(status_code=404, detail="Carro não encontrado.")