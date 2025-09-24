"""Этот файл содержит точку входа для запуска приложения с использованием Uvicorn."""

from fastapi import FastAPI
from src.api.users import router as router_users


app = FastAPI()
app.include_router(router_users)


@app.get('/')
async def main():
    return {'Hello ITK academy!'}