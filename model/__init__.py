import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base
from model.encomenda import Encomenda  # força registro da tabela

# Caminho absoluto para o diretório model/database/
DB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database'))
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

# Caminho do arquivo SQLite
DB_PATH = os.path.join(DB_DIR, 'db_encomenda.sqlite3')
DB_URL = f"sqlite:///{DB_PATH}"

print(f"📌 BANCO EM USO: {DB_PATH}")

engine = create_engine(DB_URL, echo=False)
Session = sessionmaker(bind=engine)

# Cria as tabelas apenas se o arquivo ainda não existir
if not os.path.exists(DB_PATH):
    print("⚙️ Criando banco e tabelas...")
    Base.metadata.create_all(engine)
else:
    print("✅ Banco já existente.")