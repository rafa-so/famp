from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from app.models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algorítmos e Lógica de Programação",
        "aulas": 87,
        "horas": 10
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso
