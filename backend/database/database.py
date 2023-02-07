from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DB_PASS, DB_HOST, DB_PORT, DB_NAME, DB_USER

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)