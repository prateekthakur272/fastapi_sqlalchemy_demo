### Prateek Thakur 2024
# Imports
from fastapi import FastAPI
from uvicorn import run
# Routes
from routes.routes import router

app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    run('main:app', reload=True, port=5000)