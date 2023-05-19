from fastapi import APIRouter


router = APIRouter()


@router.get('/api/v1/usuarios')
async def get_usuarios():
    return { "info": "lista todos os usuários" }
