from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras')
        return value

cursos = [
    Curso(titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(titulo="Programação em Python", aulas=115, horas=30)
]
