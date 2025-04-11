from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from model import Base

class Encomenda(Base):
    __tablename__ = 'encomenda'

    id = Column("encomenda_id", Integer, primary_key=True)
    nome = Column(String(150), unique=False)
    casa = Column(String(100))
    quantidade_p = Column(Integer)
    pacote = Column(String(10))
    cep = Column(String(10))
    endereco = Column(String(150))
    data_cadastro = Column(DateTime, default=datetime.now)  # CORRIGIDO

    def __init__(self, nome: str, casa: str, quantidade_p: int,
                 pacote: str, cep: str, endereco: str,
                 data_cadastro: Union[datetime, None] = None):

        self.nome = nome
        self.casa = casa
        self.quantidade_p = quantidade_p
        self.pacote = pacote
        self.cep = cep
        self.endereco = endereco
        self.data_cadastro = data_cadastro or datetime.now()  # CORRIGIDO



