from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import Depends

from typing import Optional, Any, List

from time import sleep

from app.models import Curso
from app.models import cursos

def fake_db():
    try:
        print("Abrindo conexão com bando de dados...")
        sleep(1)
    finally:
        print("Fechando conexão com o banco de dados...")
        sleep(1)

app = FastAPI(
    title='API de cursos da Geek University',
    version='0.0.1',
    description='Uma API para estudo do FastAPI'
)


@app.get('/cursos',
         description='Retorna tudos os cursos ou uma lista vazia',
         summary='Retorna todos os cursos',
         response_model=List[Curso],
         response_description="Cursos encontrados com sucesso")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None,
                                         title="ID do Curso",
                                         description='Deve ser entre um e dois',
                                         gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    curso.id = next_id
    cursos.append(curso)

    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Não existe um curso com o id {curso_id}")

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Não existe um curso com o id {curso}")


@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5),
                   b: int = Query(default=None, gt=10 ),
                   c: Optional[int] = None,
                   x_geek: str = Header(default=None) ):
    soma = a + b + c
    print(f"X-GEEK: {x_geek}")
    return { "resultado": soma }
