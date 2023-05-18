from fastapi import FastAPI

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


