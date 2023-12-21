import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
MYSQL_URL = os.getenv('MYSQL_URL')

Base = declarative_base()

db = create_engine(MYSQL_URL)
Session = sessionmaker(autocommit=False, bind=db)
Base.metadata.create_all(bind=db)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()