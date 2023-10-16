from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .parsing_tg.router import router as router_parsing  


app = FastAPI(
    title="Parsing API"
)
# 
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8081",
]

app.mount("/Photos", StaticFiles(directory=r"src\Photos"), name="Photos")
# app.mount("/Photos", StaticFiles(directory=r"src/Photos"), name="Photos")

app.add_middleware(
    CORSMiddleware,
     allow_origins=origins, 
     allow_credentials=True, 
     allow_methods=["*"], 
     allow_headers=["*"], 
)
app.include_router(router_parsing)
