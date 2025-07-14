from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from models import Pedido
from convert import carregar_csv_para_sqlite, engine

app = FastAPI()

# Opcional: carregar dados no banco (pode fazer isso antes de rodar a API)
carregar_csv_para_sqlite('./20250702_Pedidos_csv_2025.csv')

@app.get("/pedidos/{pedido_id}", response_model=Pedido)
def get_pedido(pedido_id: int):
    with Session(engine) as session:
        statement = select(Pedido).where(Pedido.IdPedido == pedido_id)
        pedido = session.exec(statement).first()
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
        return pedido
