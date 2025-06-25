from pydantic import BaseModel

class Livros(BaseModel):
    id : int
    titulo : str
    autor : str
    ano_publicacao : str
    disponivel : bool
