from sqlalchemy import *
from base_de_dados.database import engine

from sqlalchemy.orm import sessionmaker
from base_de_dados.models import Aluno

Session = sessionmaker(bind=engine)






def consultar_alunos():
    session = Session()

    try:
        alunos = session.query(Aluno).all()
        if alunos:
            for aluno in alunos :
                return f"Nome: {aluno.nome} ID:{aluno.id_aluno}"
    finally:   
        session.close()
    
    



def consultar_aluno_por_nome(nome):
    session = Session()
    aluno = session.query(Aluno).filter_by(nome=nome).first()
    return f"Nome: {aluno.nome} ID: {aluno.id_aluno}"
    
    



def adicionar_aluno(nome_aluno):
    session = Session() 

    try:
        aluno_existente = session.query(Aluno).filter_by(nome=nome_aluno).first()

        if aluno_existente:
            return "Aluno já cadastrado"

        novo_aluno = Aluno(nome=nome_aluno)
        session.add(novo_aluno)

        session.commit() 
        return "Aluno cadastrado com sucesso"

    except Exception as e:
        session.rollback()  
        return f"Erro ao cadastrar aluno: {e}"

    finally:
        session.close()  