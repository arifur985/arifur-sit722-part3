from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://task7_i4ka_user:sOHKZjZnf3cVOUnkJL4jWZDicURnXTg3@dpg-crtaf4ogph6c7396kvj0-a.oregon-postgres.render.com/task7_i4ka" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
