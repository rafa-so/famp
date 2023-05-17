from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return { "msg": "FastAPI na geek University" }
