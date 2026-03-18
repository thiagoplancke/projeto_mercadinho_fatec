from database import engine
from sqlalchemy.orm import sessionmaker
from models import Aluno

Session = sessionmaker(bind=engine)
session = Session()

novo_aluno = Aluno(nome="Thiago")

session.add(novo_aluno)
session.commit()

from models import Produto

produto = Produto(
    nome="Coca-Cola",
    preco_unitario=5.0,
    estoque=10
)

session.add(produto)
session.commit()