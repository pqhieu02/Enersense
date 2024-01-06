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


async def create_db():
    # poolclass=NullPool is extremely efficient since it creats a db connection every time an operation is registered
    # This is temporary fix for unresolved error
    db = create_async_engine(MYSQL_URL_ASYNC, poolclass=NullPool)

    async with db.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    return db

db = asyncio.run(create_db())
Session = sessionmaker(autocommit=False, bind=db, class_=AsyncSession)


def db_session():
    return Session
