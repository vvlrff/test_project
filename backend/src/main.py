from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi_pagination import add_pagination

from .api.router import router as router_orm
from .supp_bot.router import router as router_bot
from .parsing_tg.router import router as router_parsing  
from .elastic_search.router import router as router_search
print(router_search)
# from .parsing.router import router as router_parsing
# from .output.router import router as router_output

app = FastAPI(
    title="Hack API"
)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",

    "http://localhost:3000",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
     allow_origins=origins, 
     allow_credentials=True, 
     allow_methods=["*"], 
     allow_headers=["*"], 
)

app.include_router(router_search)
app.include_router(router_orm)
app.include_router(router_bot)
app.include_router(router_parsing)
