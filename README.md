
# Minha API em REST

Este pequeno projeto faz parte do material didático da disciplina **Desenvolvimento Full Stack**.

O projeto consiste em uma **API REST**, integrada a uma **API externa da ViaCEP** e a uma interface (front-end). A API realiza consultas por CEP na API da ViaCEP para identificar o endereço correto das pessoas. A proposta é criar um sistema de encomendas para uma determinada região, com o objetivo de impulsionar a efetividade de uma empresa que realiza entregas por conta própria.

O objetivo aqui é apresentar uma API implementada seguindo o estilo **REST**.

## Tecnologias utilizadas

- Flask  
- SQLAlchemy  
- OpenAPI 3  
- SQLite  

---

## Instalação

Será necessário ter todas as libs Python listadas no `requirements.txt` instaladas. Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/).

```bash
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas descritas no arquivo `requirements.txt`.

---

## Executando o servidor

Para executar a API basta executar:

```bash
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro `--reload`, que reiniciará o servidor automaticamente após uma mudança no código-fonte:

```bash
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

---

## Como executar através do Docker

Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o `Dockerfile` e o `requirements.txt` no terminal. Execute como administrador o seguinte comando para construir a imagem Docker:

```bash
$ docker build -t rest-api .
```

ou

```bash
$ docker build -t rest-api ./minhaapi
```

Uma vez criada a imagem, para executar o container basta rodar o seguinte comando como administrador:

```bash
$ docker run -p 5000:5000 rest-api
```

Acesse a API em: [http://localhost:5000/#/](http://localhost:5000/#/)

---

## Alguns comandos úteis do Docker

Verificar imagens criadas:

```bash
$ docker images
```

Remover uma imagem:

```bash
$ docker rmi <IMAGE ID>
```

Verificar containers em execução:

```bash
$ docker container ls --all
```

Parar um container:

```bash
$ docker stop <CONTAINER ID>
```

Remover um container:

```bash
$ docker rm <CONTAINER ID>
```

Para mais comandos, consulte a [documentação oficial do Docker](https://docs.docker.com/).