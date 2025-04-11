import os

db_path = os.path.abspath("database/meu_banco.sqlite3")
db_url = f"sqlite:///{db_path}"
print(f"URL de acesso ao banco: {db_url}")