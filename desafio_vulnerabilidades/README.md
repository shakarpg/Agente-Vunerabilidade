# Desafio DIO - Criação de Cenários Controlados para Vulnerabilidades

## Descrição
Projeto para simulação e estudo de vulnerabilidades em aplicações, utilizando FastAPI, Uvicorn e integração opcional com Cytoscape.

## Estrutura
- **app/main.py**: Backend com FastAPI.
- **app/frontend.html**: Frontend simples com Cytoscape.js.
- **requirements.txt**: Dependências do projeto.
- **images/**: Capturas de tela do projeto.
- **.github/workflows/python-app.yml**: Pipeline de CI.

## Como Executar
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse em: `http://127.0.0.1:8000`

## Objetivos
- Criar ambiente seguro para estudo de vulnerabilidades.
- Documentar processos técnicos.
- Publicar no GitHub.
