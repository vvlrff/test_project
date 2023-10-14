#!/bin/bash

alembic revision --autogenerate -m "Add user model"

alembic upgrade head

uvicorn src.main:app --host 0.0.0.0 --port 8000
