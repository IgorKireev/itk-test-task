from fastapi import FastAPI
from src.api.users import router as router_users


app = FastAPI()
app.include_router(router_users)


@app.get('/')
async def main():
    return {'Hello World!'}