from sqlmodel import SQLModel, create_engine, Session
import pandas as pd
from models import Pedido

sqlite_url = "sqlite:///pedidos.db"
engine = create_engine(sqlite_url, echo=True)

def carregar_csv_para_sqlite(
    caminho_csv: str,
    encoding: str = "utf-16",
    sep: str = ";"
):
    # Cria as tabelas no banco (se não existirem)
    SQLModel.metadata.create_all(engine)

    # Lê o CSV
    df = pd.read_csv(caminho_csv, encoding=encoding, sep=sep)

    # Converte colunas de datas para datetime.date
    for col in ['DataRegistro', 'PrazoAtendimento', 'DataResposta']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format='%d/%m/%Y', errors='coerce').dt.date

    # Converte ProtocoloPedido para string
    df['ProtocoloPedido'] = df['ProtocoloPedido'].astype(str)

    # Insere dados no banco
    with Session(engine) as session:
        for _, row in df.iterrows():
            data = row.to_dict()

            # Substitui NaN por None para evitar erros
            for key, value in data.items():
                if pd.isna(value):
                    data[key] = None

            pedido = Pedido(**data)
            session.add(pedido)

        session.commit()

    print("Dados carregados com sucesso no banco SQLite.")  