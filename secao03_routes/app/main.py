from fastapi import FastAPI


from app.routes import curso_router
from app.routes import usuario_router


app = FastAPI()
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])


