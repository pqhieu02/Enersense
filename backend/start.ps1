pip install -r requirements.txt
alembic upgrade head
uvicorn src.main:app --port 8000 --host 0.0.0.0