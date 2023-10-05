import json
import os
import random as rnd
import re
import sys

from fastapi import APIRouter, Body, Depends, File, Query, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
# from src.api.occurrencesCounter import OccurrencesCounter

from ..datebase import get_async_session
# from .utils import Clusterization

# clusterization = Clusterization()

# from .utils import get_all, get_countru, get_item, get_items_countru, get_category, get_items_category, get_items_net_href_, get_net_href
# from . import shemas
# from fastapi_pagination import Page, paginate

router = APIRouter (
    prefix='/api',
    tags= ['api']
)

# @router.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     folder_path = os.getcwd() + r'\src\api\INPUT_\\'  # путь к папке, в которую нужно сохранить файл
#     # print(folder_path)
#     file_path = os.path.join(folder_path, file.filename)  # объединяем путь к папке и имени файла
#     client_dir = 'front\pdf'
    
#     with open(file_path, "wb") as f:  # открываем файл на запись
#         f.write(await file.read())  # записываем содержимое загруженного файла в созданный файл
# # front\pdf

#     parent = os.path.join(os.getcwd(), os.pardir) 
#     client_path = parent[:-10] + client_dir
#     client_path = os.path.join(client_path, file.filename)
#     print(client_path)
#     # with open(client_path, "wb") as f:  # открываем файл на запись
#     #     f.write(await file.read())

#     return {"file": file}

# @router.get("/upload_test")
# async def upload_file():
#     res = clusterization.main()
#     data = res 
#     print(len(res))
#     # res = [{'category': 'Категория 1', 'description': 'геодезический чание выработка отчёт инженерногеологический ', 'amount': 2, 'file_names': ['Документация1\\╨а╨░╨╖╨┤╨╡╨╗ ╨Я╨Ф тДЦ10_╨в╨╛╨╝ 10.1_51-10.00027-21_╨б╨Ъ╨н-25982.pdf', 'Документация2\\╨в╨╛╨╝ 2_╨Ш╨╖╨╝.1.00001-21_╨Х╨У╨н-26404.pdf']}, {'category': 'Категория 2', 'description': 'примечание обозначение подъезд ание махачкала ', 'amount': 1, 'file_names': ['Документация1\\╨Ш╨г╨Ы ╨а╨░╨╖╨┤╨╡╨╗ ╨Я╨Ф тДЦ10.5.00027-21_╨б╨Ъ╨н-25982.pdf']}, {'category': 'Категория 3', 'description': 'энергетический эффективность блок зам архитектурный ', 'amount': 1, 'file_names': ['Документация2\\╨а╨░╨╖╨┤╨╡╨╗ ╨Я╨Ф тДЦ3_╨Ш╨╖╨╝.2.00001-21_╨Х╨У╨н-26404.pdf']}, {'category': 'Категория 4', 'description': 'холодный гудермес ножовка день метеостанция ', 'amount': 2, 'file_names': ['Документация1\\╨а╨░╨╖╨┤╨╡╨╗ ╨Я╨Ф тДЦ1_╨в╨╛╨╝ 1_51-╨Я╨Ч.00027-21_╨б╨Ъ╨н-25982.pdf', 'Документация1\\╨а╨░╨╖╨┤╨╡╨╗ ╨Я╨Ф тДЦ2_╨в╨╛╨╝ 2_51-╨Я╨Я╨Ю.00027-21_╨б╨Ъ╨н-25982.pdf']}, {'category': 'Категория 5', 'description': 'месторождение обустройство гарюшкинский строительство куст ', 'amount': 2, 'file_names': ['Документация2\\╨а╨░╨╖╨┤╨╡╨╗ ╨Я╨Ф тДЦ1 ╨з╨░╤Б╤В╤М тДЦ2 ╨Ш╨╖╨╝.1.00001-21_╨Х╨У╨н-26404.pdf', 'Документация2\\╨а╨░╨╖╨┤╨╡╨╗ ╨Я╨ФтДЦ6 ╨з╨░╤Б╤В╤М тДЦ3_╨Ш╨╖╨╝.1.00001-21_╨Х╨У╨н-26404.pdf']}]
#     return JSONResponse(data)

# @router.get("/result/{name_file}")
# async def result_file(name_file: str):
#     print(f'Есть контакт : {name_file}')
#     data = {'pages': [1, 2, 4, 5, 6],
#             'differensse': ['А и Б сидело на трубе', 'Конь идет по борозде']}
#     return data

# @router.get("/one_classification/{iunput_user}")
# async def one_classification(iunput_user : str):
#     print(iunput_user)
#     iunput_user = iunput_user.replace('\n', ' ')
#     print(iunput_user)
#     # print( OccurrencesCounter.ENTERY_POINT )
#     OccurrencesCounter.ENTERY_POINT = sys.path[0] + "\\src\\api\\INPUT_"
#     # print( OccurrencesCounter.ENTERY_POINT )
#     data = OccurrencesCounter.main(iunput_user)
    
#     return {"data":data} 

# @router.post("/one_classification_list/{iunput_user}")
# async def one_classification_list(iunput_user : str, data_: list):
#     print(data_)
#     # iunput_user = iunput_user.replace('\n', ' ')
#     # print(iunput_user)
#     # OccurrencesCounter.ENTERY_POINT = sys.path[0] + "\\src\\api\\INPUT_"
#     # data = OccurrencesCounter.main(iunput_user)
    
#     return {"data":data_} 

# @router.get("/get_data")
# async def get_data(session: AsyncSession = Depends(get_async_session), 
#                    page: int = Query(ge=0, default=0), 
#                    size: int = Query(ge=1, default=25)) -> Page[shemas.RawData]:
    
#     res = await get_all(session)
#     return paginate(res)

# @router.get('/get_data/id')
# async def get_item_(session: AsyncSession = Depends(get_async_session),
#                     id: int = Query()):
#     res = await get_item(session, id)
#     return res

# @router.get('/get_data/countrus')
# async def get_countru_(session: AsyncSession = Depends(get_async_session)):
#     res = await get_countru(session)
#     return res



# @router.get('/get_data/countru')
# async def get_item_countru(session: AsyncSession = Depends(get_async_session),
#                     countru: str = Query(),
#                     page: int = Query(ge=0, default=0), 
#                     size: int = Query(ge=1, default=25)) -> Page[shemas.RawData]:
#     res = await get_items_countru(session, countru)
#     return paginate(res)

# @router.get('/get_data/category')
# async def get_category_(session: AsyncSession = Depends(get_async_session)):
#     res = await get_category(session)
#     return res

# @router.get('/get_data/category_')
# async def get_items_category_(session: AsyncSession = Depends(get_async_session),
#                     category: str = Query(),
#                     page: int = Query(ge=0, default=0), 
#                     size: int = Query(ge=1, default=25)) -> Page[shemas.RawData]:
    
#     res = await get_items_category(session,category)
#     return paginate(res)


# @router.get('/get_data/sites')
# async def get_data_site(session: AsyncSession = Depends(get_async_session)):
    
#     res = await get_net_href(session)
#     return res

# @router.get('/get_data/sites_')
# async def get_items_sites_(session: AsyncSession = Depends(get_async_session),
#                     sites: str = Query(),
#                     page: int = Query(ge=0, default=0), 
#                     size: int = Query(ge=1, default=25)) -> Page[shemas.RawData]:
    
#     res = await get_items_net_href_(session,sites)
#     return paginate(res)