from models import Pedido
from fastapi import FastAPI,HTTPException
import pandas as pd

df = pd.read_csv('./20250702_Pedidos_csv_2025.csv', encoding='utf-16', sep=';')

# Converte colunas de data de string para datetime.date
for col in ['DataRegistro', 'PrazoAtendimento', 'DataResposta']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], format='%d/%m/%Y', errors='coerce').dt.date

# Converte ProtocoloPedido para string
df['ProtocoloPedido'] = df['ProtocoloPedido'].astype(str)

app = FastAPI()

@app.get("/pedidos/{pedido}", response_model= Pedido)
def get_pedido(pedido: int):

    request = df[df["IdPedido"] == pedido]

    if request.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    pedido_dict = request.iloc[0].to_dict()

    return pedido_dict