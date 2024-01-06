import asyncio
import os
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
MYSQL_URL_ASYNC = os.getenv('MYSQL_URL_ASYNC')
Base = declarative_base()

db = create_async_engine(MYSQL_URL_ASYNC, poolclass=NullPool)

async def create_tables():
    async with db.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return db

Session = sessionmaker(autocommit=False, bind=db, class_=AsyncSession)

async def get_db():
    session = Session()
    try:
        yield session
    finally:
        await session.close()