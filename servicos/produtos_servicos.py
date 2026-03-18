from base_de_dados.database import engine

from sqlalchemy.orm import sessionmaker
from base_de_dados.models import Produto

Session = sessionmaker(bind=engine)


def adicionar_produto(nome_produto,preco,qntd):
    session = Session() 

    try:
        produto_existente = session.query(Produto).filter_by(nome=nome_produto).first()

        if produto_existente:
            return "Produto já cadastrado"

        novo_produto = Produto(nome=nome_produto,preco_unitario = preco, estoque = qntd)
        session.add(novo_produto)

        session.commit()  
        return "Produto cadastrado com sucesso"

    except Exception as e:
        session.rollback()  
        return f"Erro ao cadastrar o produto: {e}"

    finally:
        session.close()




def consultar_produtos():
    session = Session()

    try:
        produtos = session.query(Produto).all()
        if produtos:
            for produto in produtos :
                print(f"Nome: {produto.nome} / Preço: R${produto.preco_unitario} / Estoque: {produto.estoque} / ID: {produto.id_produto}")
    finally:   
        session.close()
    
    



def consultar_produto_por_nome(nome):
    session = Session()
    try:
        produto = session.query(Produto).filter_by(nome=nome).first()
        if produto:
            return f"Nome: {produto.nome} / Preço: R${produto.preco_unitario} / Estoque: {produto.estoque} / ID: {produto.id_produto}"
        return "Produto não existe"
    finally:   
        session.close()