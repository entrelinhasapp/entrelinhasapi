from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "API está online!"})


# Rota dinâmica (GET)
@app.get("/livros/{id_livro}/")
def dados_livro(id_livro: int):
    df = pd.read_csv('https://raw.githubusercontent.com/entrelinhasapp/entrelinhasapi/refs/heads/main/db_livros.csv')
    #df = pd.read_csv('db_livros.csv', encoding='utf-8')

    df = df[df['ID livro'] == id_livro]


    #return JSONResponse(content=dic_info)
    return JSONResponse(content=df.to_dict(orient="records")[0])


