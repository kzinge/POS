from pydantic import BaseModel, constr
from typing import Optional
from datetime import date

class Pedido(BaseModel):
    IdPedido: int
    ProtocoloPedido: constr(max_length=17)
    Esfera: constr(max_length=30)
    UF: Optional[constr(max_length=2)] = None
    Municipio: Optional[constr(max_length=200)] = None
    OrgaoDestinatario: constr(max_length=250)
    Situacao: constr(max_length=200)
    DataRegistro: date
    PrazoAtendimento: date
    FoiProrrogado: constr(max_length=3)  # "Sim" ou "Não"
    FoiReencaminhado: constr(max_length=3)  # "Sim" ou "Não"
    FormaResposta: constr(max_length=200)
    OrigemSolicitacao: constr(max_length=50)
    IdSolicitante: int
    AssuntoPedido: constr(max_length=200)
    SubAssuntoPedido: constr(max_length=200)
    Tag: constr(max_length=1024)
    DataResposta: Optional[date] = None
    Decisao: Optional[constr(max_length=100)] = None
    EspecificacaoDecisao: Optional[constr(max_length=200)] = None
