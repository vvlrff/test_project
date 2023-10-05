from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi_pagination import add_pagination

from .api.router import router as router_orm
# from .parsing.router import router as router_parsing
# from .output.router import router as router_output

app = FastAPI(
    title="Hack API"
)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
     allow_origins=origins, 
     allow_credentials=True, 
     allow_methods=["*"], 
     allow_headers=["*"], 
)


app.include_router(router_orm)
# app.include_router(router_parsing)
# app.include_router(router_output)
# add_pagination(app) 