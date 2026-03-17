
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from database import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id_aluno = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(25))


class Produto(Base):
    __tablename__ = "produtos"

    id_produto = Column(Integer, primary_key=True, autoincrement= True)
    nome = Column(String(40),nullable=False)
    preco_unitario = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)


class Compra(Base):
    __tablename__ = "compras"

    id_compra = Column(Integer, primary_key=True, autoincrement= True)
    aluno_id = Column(Integer, ForeignKey("alunos.id_aluno"))
    valor_total = Column(Float)

class ItemCompra(Base):
    __tablename__="itens_compras"

    id = Column(Integer, primary_key= True )
    compra_id = Column(Integer, ForeignKey("compras.id_compra"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id_produto"), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable= False)