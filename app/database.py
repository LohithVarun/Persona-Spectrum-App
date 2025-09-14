# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite"
# For PostgreSQL later:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # check_same_thread is only for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is already defined in schemas.py, so we should import it to avoid re-defining
# from .schemas import Base # <<< Uncomment this if you remove Base = declarative_base() from schemas.py
# For now, if Base is defined in schemas.py and passed to metadata.create_all,
# it should ideally be imported. However, for a single, small project this way is common.
# If you run into issues with tables not creating, you might need to move declarative_base() to database.py
# and import Base from here into schemas.py, or simply ensure schemas.py is imported before metadata.create_all

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()