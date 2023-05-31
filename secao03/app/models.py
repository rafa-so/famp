from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras.')
        if value.islower():
            raise ValueError("O título deve ser capitalizado.")
        return value

    @validator('aulas')
    def valida_aulas(cls, value: int):
        if value < 12:
            raise ValueError('Não pode haver mais de 12 aulas por curso.')
        return value

    @validator('horas')
    def valida_horas(cls, value: int):
        if value < 3:
            raise ValueError('Não pode haver curso com menos de três horas de duração.')
        return value

cursos = [
    Curso(titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(titulo="Programação em Python", aulas=115, horas=30)
]
