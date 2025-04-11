from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc
import requests
from pydantic import ValidationError

from model import Session, Encomenda
from schemas.encomenda import EncomendaSchema, EncomendaBuscaSchema, EncomendaViewSchema, \
    ListagemEncomendasSchema, EncomendaDelSchema, apresenta_encomendas, apresenta_encomenda, \
    CepBuscaSchema, EnderecoViaCEPSchema
from schemas.error import ErrorSchema
from flask_cors import CORS

info = Info(title="minhaapi", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
encomenda_tag = Tag(name="Encomenda", description="Consultar, incluir, atualizar e excluir a encomenda do cadastro")
via_cep_tag = Tag(name="ViaCEP", description="Consulta de endereço a partir do CEP usando API pública")


@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')


@app.post('/encomenda', tags=[encomenda_tag],
          responses={"200": EncomendaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_encomenda():
    """Cadastra nova encomenda (aceita dados via FormData)"""
    try:
        form = EncomendaSchema(**request.form)
    except ValidationError as e:
        return {"mensagem": "Erro de validação", "erros": e.errors()}, 422

    encomenda = Encomenda(
        nome=form.nome,
        casa=form.casa,
        cep=form.cep,
        endereco=form.endereco,
        quantidade_p=form.quantidade_p,
        pacote=form.pacote
    )

    try:
        session = Session()
        session.add(encomenda)
        session.commit()
        return apresenta_encomenda(encomenda), 200

    except IntegrityError as e:
        session.rollback()
        return {"mensagem": f"Encomenda de '{encomenda.nome}' já existente, verifique!"}, 409

    except Exception as e:
        session.rollback()
        return {"mensagem": "Erro ao gravar a encomenda."}, 400


@app.put('/encomenda', tags=[encomenda_tag],
         responses={"200": EncomendaViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def atualizar_encomenda():
    """Atualiza uma encomenda existente (recebe dados via FormData)"""
    try:
        form = EncomendaSchema(**request.form)
    except ValidationError as e:
        return {"mensagem": "Erro de validação", "erros": e.errors()}, 422

    session = Session()
    encomenda = session.query(Encomenda).filter_by(nome=form.nome).first()

    if not encomenda:
        return {"mensagem": "Encomenda não encontrada"}, 404

    try:
        encomenda.casa = form.casa
        encomenda.cep = form.cep
        encomenda.endereco = form.endereco
        encomenda.quantidade_p = form.quantidade_p
        encomenda.pacote = form.pacote

        session.commit()
        return apresenta_encomenda(encomenda), 200

    except Exception as e:
        session.rollback()
        return {"mensagem": "Erro ao atualizar a encomenda"}, 400


@app.get('/listar_encomendas', tags=[encomenda_tag],
         responses={"200": ListagemEncomendasSchema, "404": ErrorSchema})
def listar_encomendas():
    session = Session()
    encomendas = session.query(Encomenda).order_by(asc(Encomenda.nome)).all()
    return apresenta_encomendas(encomendas), 200


@app.delete('/encomenda', tags=[encomenda_tag],
            responses={"200": EncomendaDelSchema, "404": ErrorSchema})
def del_encomenda(query: EncomendaBuscaSchema):
    encomenda_nome = unquote(unquote(query.nome))
    session = Session()
    count = session.query(Encomenda).filter(Encomenda.nome == encomenda_nome).delete()
    session.commit()

    if count:
        return {"mensagem": "encomenda removida", "nome": encomenda_nome}, 200
    else:
        return {"mensagem": "encomenda não existente!"}, 404


@app.get('/endereco', tags=[via_cep_tag],
         responses={"200": EnderecoViaCEPSchema, "400": ErrorSchema, "404": ErrorSchema})
def buscar_endereco_por_cep(query: CepBuscaSchema):
    cep = query.cep.replace("-", "").strip()

    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            return {"mensagem": "CEP não encontrado"}, 404

        return {
            "cep": dados["cep"],
            "logradouro": dados["logradouro"],
            "bairro": dados["bairro"],
            "cidade": dados["localidade"],
            "estado": dados["uf"]
        }, 200

    except Exception as e:
        return {"mensagem": "Erro ao consultar o endereço"}, 400


if __name__ == '__main__':
    app.run(debug=True)


