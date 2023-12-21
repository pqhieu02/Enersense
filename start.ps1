alembic upgrade head
uvicorn src.__init__:app --port 8000 --host 0.0.0.0