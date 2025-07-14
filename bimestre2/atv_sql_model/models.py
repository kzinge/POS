from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class Pedido(SQLModel, table=True):
    IdPedido: int = Field(primary_key=True)
    ProtocoloPedido: Optional[str] = Field(default=None, max_length=17)
    Esfera: Optional[str] = Field(default=None, max_length=30)
    UF: Optional[str] = Field(default=None, max_length=2)
    Municipio: Optional[str] = Field(default=None, max_length=200)
    OrgaoDestinatario: Optional[str] = Field(default=None, max_length=250)
    Situacao: Optional[str] = Field(default=None, max_length=200)
    DataRegistro: Optional[date] = None
    PrazoAtendimento: Optional[date] = None
    FoiProrrogado: Optional[str] = Field(default=None, max_length=3)  # "Sim" ou "Não"
    FoiReencaminhado: Optional[str] = Field(default=None, max_length=3)  # "Sim" ou "Não"
    FormaResposta: Optional[str] = Field(default=None, max_length=200)
    OrigemSolicitacao: Optional[str] = Field(default=None, max_length=50)
    IdSolicitante: Optional[int] = None
    AssuntoPedido: Optional[str] = Field(default=None, max_length=200)
    SubAssuntoPedido: Optional[str] = Field(default=None, max_length=200)
    Tag: Optional[str] = Field(default=None, max_length=1024)
    DataResposta: Optional[date] = None
    Decisao: Optional[str] = Field(default=None, max_length=100)
    EspecificacaoDecisao: Optional[str] = Field(default=None, max_length=200)
