from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .shemas import *
from .datebase import PG_DB
from ..elastic_search.main import IntellectualSearch
from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..datebase import get_async_session


router = APIRouter (
    prefix='/api',
    tags= ['api']
)


# @router.get('/test_new')
# async def test(session: AsyncSession = Depends(get_async_session)):
#     db = PG_DB(session)
#     data = await db.get_all_info_true()
#     return data

@router.get('/test_{param}')
async def test(param: str):
    if (param == "old"):
        ...
        # data = await db.get_all_info_true_old()
    data = [
                {
                  "id": 217,
                  "MESSAGE_ID": 986,
                  "url": "https://t.me/recipe_zuma",
                  "CHAT_TITLE": "Рецепты Zuma",
                  "date": "2023-10-15T05:21:36",
                  "msg": "Это такое лакомство, и его удивительно просто приготовить! Получается очень эффектная закуска или канапе на Новый год! Свекла окрашивает лосось снаружи, создавая красивый пурпурно-оранжевый градиент. 180 г сырой свеклы, натертой на крупной терке 100 г морской соли 70 г сахара тростниковый 40 г свежего укропа, мелко нарезанного Цедра 1 лимона 3 столовые ложки свеженатёртого хрена Щедрая щепотка свежемолотого черного перца 500 г филе лосося 1. Смешайте все ингредиенты (кроме филе лосося). 2. Выложите 1 3 смеси в форму для запекания, застеленную пищевой пленкой, и сверху выложите филе лосося (кожей вниз). По мере застывания лосось выделяет жидкость, поэтому не кладите его на плоскую тарелку. 3. Выложите на филе оставшуюся часть свекольной смеси так, чтобы мякоть была полностью покрыта. Прижмите его к мякоти лосося. 4. Плотно заверните лосося в пищевую пленку и положите сверху груз, чтобы ускорить процесс. Оставьте в холодильнике на 48 часов для застывания. 5. Через 2 дня разверните рыбу, слейте жидкость и соскребите свекольную смесь. Протрите лосося влажным кухонным полотенцем, а затем высушите. 6. Заверните лосось в пищевую пленку и положите обратно в холодильник до подачи. 7. Для подачи: нарежьте острым ножом, срезая кончик внизу, чтобы не осталось кожицы. Подавайте со сливками, лимонным соком и свежим укропом на ржаном хлебе или блинах.",
                  "photo": "https://cdn-storage-media.tass.ru/tass_media/2022/03/02/B/1646255279306084_BclUp0vj.png?w=1359"
                },
                                {
                  "id": 217,
                  "MESSAGE_ID": 986,
                  "url": "https://t.me/recipe_zuma",
                  "CHAT_TITLE": "Рецепты Zuma",
                  "date": "2023-10-15T05:21:36",
                  "msg": "Это такое лакомство, и его удивительно просто приготовить! Получается очень эффектная закуска или канапе на Новый год! Свекла окрашивает лосось снаружи, создавая красивый пурпурно-оранжевый градиент. 180 г сырой свеклы, натертой на крупной терке 100 г морской соли 70 г сахара тростниковый 40 г свежего укропа, мелко нарезанного Цедра 1 лимона 3 столовые ложки свеженатёртого хрена Щедрая щепотка свежемолотого черного перца 500 г филе лосося 1. Смешайте все ингредиенты (кроме филе лосося). 2. Выложите 1 3 смеси в форму для запекания, застеленную пищевой пленкой, и сверху выложите филе лосося (кожей вниз). По мере застывания лосось выделяет жидкость, поэтому не кладите его на плоскую тарелку. 3. Выложите на филе оставшуюся часть свекольной смеси так, чтобы мякоть была полностью покрыта. Прижмите его к мякоти лосося. 4. Плотно заверните лосося в пищевую пленку и положите сверху груз, чтобы ускорить процесс. Оставьте в холодильнике на 48 часов для застывания. 5. Через 2 дня разверните рыбу, слейте жидкость и соскребите свекольную смесь. Протрите лосося влажным кухонным полотенцем, а затем высушите. 6. Заверните лосось в пищевую пленку и положите обратно в холодильник до подачи. 7. Для подачи: нарежьте острым ножом, срезая кончик внизу, чтобы не осталось кожицы. Подавайте со сливками, лимонным соком и свежим укропом на ржаном хлебе или блинах.",
                  "photo": "https://cdn-storage-media.tass.ru/tass_media/2022/03/02/B/1646255279306084_BclUp0vj.png?w=1359"
                },
                                {
                  "id": 217,
                  "MESSAGE_ID": 986,
                  "url": "https://t.me/recipe_zuma",
                  "CHAT_TITLE": "Рецепты Zuma",
                  "date": "2023-10-15T05:21:36",
                  "msg": "Это такое лакомство, и его удивительно просто приготовить! Получается очень эффектная закуска или канапе на Новый год! Свекла окрашивает лосось снаружи, создавая красивый пурпурно-оранжевый градиент. 180 г сырой свеклы, натертой на крупной терке 100 г морской соли 70 г сахара тростниковый 40 г свежего укропа, мелко нарезанного Цедра 1 лимона 3 столовые ложки свеженатёртого хрена Щедрая щепотка свежемолотого черного перца 500 г филе лосося 1. Смешайте все ингредиенты (кроме филе лосося). 2. Выложите 1 3 смеси в форму для запекания, застеленную пищевой пленкой, и сверху выложите филе лосося (кожей вниз). По мере застывания лосось выделяет жидкость, поэтому не кладите его на плоскую тарелку. 3. Выложите на филе оставшуюся часть свекольной смеси так, чтобы мякоть была полностью покрыта. Прижмите его к мякоти лосося. 4. Плотно заверните лосося в пищевую пленку и положите сверху груз, чтобы ускорить процесс. Оставьте в холодильнике на 48 часов для застывания. 5. Через 2 дня разверните рыбу, слейте жидкость и соскребите свекольную смесь. Протрите лосося влажным кухонным полотенцем, а затем высушите. 6. Заверните лосось в пищевую пленку и положите обратно в холодильник до подачи. 7. Для подачи: нарежьте острым ножом, срезая кончик внизу, чтобы не осталось кожицы. Подавайте со сливками, лимонным соком и свежим укропом на ржаном хлебе или блинах.",
                  "photo": "https://cdn-storage-media.tass.ru/tass_media/2022/03/02/B/1646255279306084_BclUp0vj.png?w=1359"
                },
                ]
    return data

@router.get('/test/{id}')
async def test_for_id():
    # db = PG_DB(session)
    # data = await db.test_for_id(id)
    data =   {
    "id": 108,
    "MESSAGE_ID": 356,
    "url": "https://t.me/PobedaAirlines",
    "CHAT_TITLE": "Авиакомпания «Победа»",
    "date": "2023-10-15T07:01:40",
    "msg": "Летим в Питер со скидкой 15 Скоро пышка превратится в пончик, а парадная в подъезд, ведь промокод PITER действует последний день! Бронируйте 15 октября до 23:59 (МСК) Летите с 17 октября 2023 по 30 марта 2024 Отправляйтесь в Санкт-Петербург и обратно из городов: Москва Астрахань Владикавказ Волгоград Екатеринбург Калининград Киров Махачкала Минеральные Воды Минск Нижнекамск Новосибирск Пермь Самара Саратов Сочи Ставрополь Тюмень Ульяновск Уфа Чебоксары Челябинск Летите Победой по самым выгодным ценам только на pobeda.aero и в приложении",
    "photo": "https://cdn-storage-media.tass.ru/tass_media/2022/03/02/B/1646255279306084_BclUp0vj.png?w=1359"
  },
    return JSONResponse(data)
