from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import libraries
import asyncio

app = FastAPI()


@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>UIPath Clarke</title>
        </head>
        <body>
            <h1>Aquí no hay nada</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/synclibraries")
def sync_libraries():
    html_content = """
    <html>
        <head>
            <title>Librerías sincronizadas</title>
        </head>
        <body>
            <h1>Librerías sincronizadas</h1>
        </body>
    </html>
    """
    libraries.UpdateLibs()
    return HTMLResponse(content=html_content, status_code=200)

