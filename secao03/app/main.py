from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return { "msg": "FastAPI da seção 03" }
