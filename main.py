#bibliotecas e frameworks
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

#criar objeto de aplicação FastAPI
app = FastAPI()

#banco de dados simulado
alunos_db = {
    'joao@iterasys.com.br': {
        'nome': 'João Antonio',
        'validade assinatura': '2025-10-10',
        'endereco': 'Rua A, 123, São Paulo',
        'cep': '01000-000',
    },
    'maria@iterasys.com.br': {
        'nome': 'Maria Silva',
        'validade assinatura': '2025-05-10',
        'endereco': 'Avenida B, 456, Rio de Janeiro',
        'cep': '20000-000',
    },
    'jose@iterasys.com.br': {
        'nome': 'Jose Mario',
        'validade assinatura': '2025-07-10',
        'endereco': 'Travessa C, 789, Belo Horizonte',
        'cep': '30000-000',
    }
}

class AlunoRequest(BaseModel):
    email: EmailStr

@app.post("/buscar_aluno")    
def buscar_aluno(dados: AlunoRequest):
    aluno = alunos_db.get(dados.email)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {
        'nome_completo': aluno['nome'],
        'validade_assinatura': aluno['validade assinatura'],
    }
    
@app.post("/buscar_endereco_aluno")
def buscar_endereco_aluno(dados: AlunoRequest):
    aluno = alunos_db.get(dados.email)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {
        'nome_completo': aluno['nome'],
        'endereco': aluno['endereco'],
        'cep': aluno['cep'],
    }