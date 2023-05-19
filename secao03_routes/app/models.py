from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(titulo="Programação em Python", aulas=115, horas=30),
]
