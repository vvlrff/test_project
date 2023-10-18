# Система интеллектуального поиска для Telegram

Благодаря нашему сервису Вы можете быстро найти интересующую Вас информацию из Telegram-каналов. Мы объединили передовые алгоритмы и технологии с удобным и современным интерфейсом, чтобы предоставить пользователям быстрый и удобный доступ к необходимым данным.   

Наш сервис - это надежный и эффективный способ получить актуальную информацию из Telegram-каналов, который будет полезен как для обычных пользователей, так и для бизнеса. Мы стремимся обеспечить лучший опыт поиска и помочь Вам экономить время и усилия при поиске нужной информации.   

Нам тоже не нравится тратить время впустую, поэтому мы предлагаем Вам новый и современный взгляд на получение информации.

# Цели, задачи и особенности
## Цель:
Создание WEB-системы поиска содержимого Telegram-каналов    

## Задачи:
1) Реализация автоматизированного сбора информации Telegram-каналов;
2) Создание системы интеллектуального поиска;
3) Создание современного WEB-интерфейса;
4) Интеграция с ChatGPT.   
   
# Используемые технологии
1) FAST-API;
2) Telegram-API;
3) OpenAI-API;
4) Elasticsearch;
5) PostgreSQL;
6) React.ts.   

# Описание алгоритма решения
## Автоматизированный сбор информации Telegram-каналов:
1) Получение данных из 100 Telegram-каналов с использованием Telegram-API;
2) Наполнение информаицией БД;
3) Наполнение информацией индекса Elasticsearch;
4) Хранение медиафайлов на локальном сервере;
5) Создание механизма регулярного автоматического дополнения всех хранилищ данных.

## Создание системы интеллектуального поиска:
1) Использование высокомасштабируемой распределенной поисковой системы полнотекстового поиска и анализа данных Elasticsearch;
2) Создание индекса в Elasticsearch с морфологией русского языка и необходимыми полями;
3) Использование созданного перечня слов-синонимов русского языка (около 70000);
4) Использование нечетких алгоритмов в теле поискового запроса;
5) Ранжирование результата по релевантности или по дате сообщения.

## Создание современного WEB-интерфейса:
1) Клиентская часть на React с управлением состояния приложения redux/toolkit;
2) Применение TypeScript для типизации данных;
3) Асинхронные запросы RTK Query;
4) Масштабируемая архитектура клиентского приложения;
5) Более эффективный способ создания стилей при помощи Sass.   

## Интеграция с ChatGPT:
1) Использование OpenAI-API для интеграции возможности ответа на вопросы пользователя в WEB-сервисе;
2) Создание собственного Telegram-бота, предназначенного для ответа на вопросы пользователя (в боте реализована реферальная система, личный кабинет пользователя, сохранение истории диалога, возможность покупки токенов).   

## Ссылка на Telegram-бота:
https://t.me/AI_News_GPT_Bot   

## Ссылка на Google диск (презентация):    
https://drive.google.com/drive/folders/1TJqko7mr5ff_qnEXyAI8P-yqEbtJ5W75?usp=sharing    
   


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/

[FastApi.py]: https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png
[FastApi-url]: https://fastapi.tiangolo.com/
