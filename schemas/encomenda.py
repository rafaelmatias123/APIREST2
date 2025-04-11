from pydantic import BaseModel
from typing import List
from model.encomenda import Encomenda


class EncomendaSchema(BaseModel):
    """ Define como uma nova encomenda a ser inserida deve ser representada """
    nome: str = "Rafael-Oliveira"
    casa: str = "1A"
    cep: str = "22290-180"
    endereco: str = "Rua Marquês de São Vicente"
    quantidade_p: int = 5
    pacote: str = "P"


class EncomendaBuscaSchema(BaseModel):
    """ Define a estrutura para buscar uma encomenda pelo nome """
    nome: str = "Teste"


class CepBuscaSchema(BaseModel):
    """ Define o schema para consulta de CEP na API externa """
    cep: str = "22290-180"


class EncomendaComIdSchema(BaseModel):
    """ Schema com ID para listagem e visualização detalhada """
    id: int 
    nome: str 
    casa: str 
    cep: str 
    endereco: str 
    quantidade_p: int 
    pacote: str 



class ListagemEncomendasSchema(BaseModel):
    """ Define como uma listagem de encomendas será retornada """
    encomendas: List[EncomendaComIdSchema]


class EncomendaViewSchema(BaseModel):
    """ Define como uma encomenda será retornada com detalhes """
    id: int
    nome: str
    casa: str
    cep: str
    endereco: str
    quantidade_p: int
    pacote: str


class EncomendaDelSchema(BaseModel):
    """ Define a estrutura do dado retornado após uma requisição de remoção """
    mensagem: str
    nome: str

class EnderecoViaCEPSchema(BaseModel):
    """ Define a estrutura do dado retornado pela API ViaCEP """
    cep: str
    logradouro: str
    bairro: str
    cidade: str
    estado: str


def apresenta_encomenda(encomenda: Encomenda):
    """ Retorna a representação de uma encomenda única """
    return {
        "id": encomenda.id,
        "nome": encomenda.nome,
        "casa": encomenda.casa,
        "cep": encomenda.cep,
        "endereco": encomenda.endereco,
        "quantidade_p": encomenda.quantidade_p,
        "pacote": encomenda.pacote,
    }
def apresenta_encomendas(encomendas: List[Encomenda]):
    """ Retorna a representação das encomendas cadastradas """
    return {
        "encomendas": [
            {
                "id": e.id,
                "nome": e.nome,
                "casa": e.casa,
                "cep": e.cep,
                "endereco": e.endereco,
                "quantidade_p": e.quantidade_p,
                "pacote": e.pacote,
            } for e in encomendas
        ]
    } 