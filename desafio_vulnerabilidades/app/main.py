from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Simulador de Vulnerabilidades")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Simulador de Vulnerabilidades</h1><p>API rodando com sucesso!</p>"
