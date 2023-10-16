from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .schemas import *
from .main import IntellectualSearch


router = APIRouter(
    prefix='/search',
    tags=['search']
)


# @router.post('/test_message_date')
# async def test_search(inputuser: InputUser):
#     start_date = inputuser.start_date
#     start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")

#     end_date = inputuser.end_date
#     end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

#     search = IntellectualSearch()
#     data = search.main(inputuser.message, start_date_str, end_date_str)

#     return JSONResponse(content=data)

@router.post('/test_message_date_{param}')
async def elastic_test(param: str, inputuser: InputUser):
    start_date = inputuser.start_date
    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")

    end_date = inputuser.end_date
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    # elastic = IntellectualSearch()
    # data = elastic.sort_answer(inputuser.message, start_date_str, end_date_str, param)
    data = [
  {
    "id": 217,
    "MESSAGE_ID": 986,
    "url": "https://t.me/recipe_zuma",
    "CHAT_TITLE": "Рецепты Zuma",
    "date": "2023-10-15T05:21:36",
    "msg": "Это такое лакомство, и его удивительно просто приготовить! Получается очень эффектная закуска или канапе на Новый год! Свекла окрашивает лосось снаружи, создавая красивый пурпурно-оранжевый градиент. 180 г сырой свеклы, натертой на крупной терке 100 г морской соли 70 г сахара тростниковый 40 г свежего укропа, мелко нарезанного Цедра 1 лимона 3 столовые ложки свеженатёртого хрена Щедрая щепотка свежемолотого черного перца 500 г филе лосося 1. Смешайте все ингредиенты (кроме филе лосося). 2. Выложите 1 3 смеси в форму для запекания, застеленную пищевой пленкой, и сверху выложите филе лосося (кожей вниз). По мере застывания лосось выделяет жидкость, поэтому не кладите его на плоскую тарелку. 3. Выложите на филе оставшуюся часть свекольной смеси так, чтобы мякоть была полностью покрыта. Прижмите его к мякоти лосося. 4. Плотно заверните лосося в пищевую пленку и положите сверху груз, чтобы ускорить процесс. Оставьте в холодильнике на 48 часов для застывания. 5. Через 2 дня разверните рыбу, слейте жидкость и соскребите свекольную смесь. Протрите лосося влажным кухонным полотенцем, а затем высушите. 6. Заверните лосось в пищевую пленку и положите обратно в холодильник до подачи. 7. Для подачи: нарежьте острым ножом, срезая кончик внизу, чтобы не осталось кожицы. Подавайте со сливками, лимонным соком и свежим укропом на ржаном хлебе или блинах.",
    "photo": "http://localhost:8001/Photos/0_default.jpg"
  },
  {
    "id": 108,
    "MESSAGE_ID": 356,
    "url": "https://t.me/PobedaAirlines",
    "CHAT_TITLE": "Авиакомпания «Победа»",
    "date": "2023-10-15T07:01:40",
    "msg": "Летим в Питер со скидкой 15 Скоро пышка превратится в пончик, а парадная в подъезд, ведь промокод PITER действует последний день! Бронируйте 15 октября до 23:59 (МСК) Летите с 17 октября 2023 по 30 марта 2024 Отправляйтесь в Санкт-Петербург и обратно из городов: Москва Астрахань Владикавказ Волгоград Екатеринбург Калининград Киров Махачкала Минеральные Воды Минск Нижнекамск Новосибирск Пермь Самара Саратов Сочи Ставрополь Тюмень Ульяновск Уфа Чебоксары Челябинск Летите Победой по самым выгодным ценам только на pobeda.aero и в приложении",
    "photo": "http://localhost:8001/Photos/0_default.jpg"
  },
  {
    "id": 176,
    "MESSAGE_ID": 139,
    "url": "https://t.me/tlg_grant",
    "CHAT_TITLE": "The Grant / учеба, стажировки, гранты заграницей",
    "date": "2023-10-15T07:35:06",
    "msg": "Стипендии от University of Dayton в США Приемлемые страны : все страны. Уровень курса: бакалавриат. Дейтонский университет (UD) частный римско-католический исследовательский университет в Дейтоне, штат Огайо. В университете обучается 11 306 студентов (8 681 студент и 2 625 выпускников) из различных религиозных, этнических и географических слоев из 41 штата и 38 стран. Он предлагает более 80 академических программ в области искусства и науки, делового администрирования, образования и здравоохранения, инженерии и права. В рейтинге национальных университетов US News World Report за 2022 год Дейтонский университет занимает 132-е место в общем зачете и 58-е место в США. Финансовые преимущества: -Стипендия за заслуги: 30 000 долларов США в год. -Стипендия на учебники: 4000 долларов в течение четырех лет. Крайний срок: 1 ноября 2023 г. Подробнее:",
    "photo": "http://localhost:8001/Photos/0_default.jpg"
  },]
    return JSONResponse(content=data)

@router.post('/test_message_{param}')
async def test_search(param: str, inputuser: InputUserMessage):
    # search = IntellectualSearch()
    # data = search.sort_answer_without_date(inputuser.message, param)
    data = [
  {
    "id": 217,
    "MESSAGE_ID": 986,
    "url": "https://t.me/recipe_zuma",
    "CHAT_TITLE": "Рецепты Zuma",
    "date": "2023-10-15T05:21:36",
    "msg": "Это такое лакомство, и его удивительно просто приготовить! Получается очень эффектная закуска или канапе на Новый год! Свекла окрашивает лосось снаружи, создавая красивый пурпурно-оранжевый градиент. 180 г сырой свеклы, натертой на крупной терке 100 г морской соли 70 г сахара тростниковый 40 г свежего укропа, мелко нарезанного Цедра 1 лимона 3 столовые ложки свеженатёртого хрена Щедрая щепотка свежемолотого черного перца 500 г филе лосося 1. Смешайте все ингредиенты (кроме филе лосося). 2. Выложите 1 3 смеси в форму для запекания, застеленную пищевой пленкой, и сверху выложите филе лосося (кожей вниз). По мере застывания лосось выделяет жидкость, поэтому не кладите его на плоскую тарелку. 3. Выложите на филе оставшуюся часть свекольной смеси так, чтобы мякоть была полностью покрыта. Прижмите его к мякоти лосося. 4. Плотно заверните лосося в пищевую пленку и положите сверху груз, чтобы ускорить процесс. Оставьте в холодильнике на 48 часов для застывания. 5. Через 2 дня разверните рыбу, слейте жидкость и соскребите свекольную смесь. Протрите лосося влажным кухонным полотенцем, а затем высушите. 6. Заверните лосось в пищевую пленку и положите обратно в холодильник до подачи. 7. Для подачи: нарежьте острым ножом, срезая кончик внизу, чтобы не осталось кожицы. Подавайте со сливками, лимонным соком и свежим укропом на ржаном хлебе или блинах.",
    "photo": "http://localhost:8001/Photos/0_default.jpg"
  },
  {
    "id": 108,
    "MESSAGE_ID": 356,
    "url": "https://t.me/PobedaAirlines",
    "CHAT_TITLE": "Авиакомпания «Победа»",
    "date": "2023-10-15T07:01:40",
    "msg": "Летим в Питер со скидкой 15 Скоро пышка превратится в пончик, а парадная в подъезд, ведь промокод PITER действует последний день! Бронируйте 15 октября до 23:59 (МСК) Летите с 17 октября 2023 по 30 марта 2024 Отправляйтесь в Санкт-Петербург и обратно из городов: Москва Астрахань Владикавказ Волгоград Екатеринбург Калининград Киров Махачкала Минеральные Воды Минск Нижнекамск Новосибирск Пермь Самара Саратов Сочи Ставрополь Тюмень Ульяновск Уфа Чебоксары Челябинск Летите Победой по самым выгодным ценам только на pobeda.aero и в приложении",
    "photo": "http://localhost:8001/Photos/0_default.jpg"
  },
  {
    "id": 176,
    "MESSAGE_ID": 139,
    "url": "https://t.me/tlg_grant",
    "CHAT_TITLE": "The Grant / учеба, стажировки, гранты заграницей",
    "date": "2023-10-15T07:35:06",
    "msg": "Стипендии от University of Dayton в США Приемлемые страны : все страны. Уровень курса: бакалавриат. Дейтонский университет (UD) частный римско-католический исследовательский университет в Дейтоне, штат Огайо. В университете обучается 11 306 студентов (8 681 студент и 2 625 выпускников) из различных религиозных, этнических и географических слоев из 41 штата и 38 стран. Он предлагает более 80 академических программ в области искусства и науки, делового администрирования, образования и здравоохранения, инженерии и права. В рейтинге национальных университетов US News World Report за 2022 год Дейтонский университет занимает 132-е место в общем зачете и 58-е место в США. Финансовые преимущества: -Стипендия за заслуги: 30 000 долларов США в год. -Стипендия на учебники: 4000 долларов в течение четырех лет. Крайний срок: 1 ноября 2023 г. Подробнее:",
    "photo": "http://localhost:8001/Photos/0_default.jpg"
  },]
    return JSONResponse(content=data)

# @router.post('/test_message')
# async def test_search(inputuser: InputUserMessage):
#     search = IntellectualSearch()
#     data = search.main_without_date(inputuser.message)

#     return JSONResponse(content=data)
