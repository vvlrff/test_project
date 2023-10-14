FROM python:3.11.3

WORKDIR /server

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . .

RUN chmod a+x docker/*.sh
# 
# ВОТ это когда в первый раз запускаешь!
CMD ["sh", "-c", " alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000"]
# Это когда в следующие разы 
# CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]