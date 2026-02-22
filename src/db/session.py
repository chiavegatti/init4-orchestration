import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/orchestrator"
)
DATABASE_URL = database_url.replace("postgres://", "postgresql://")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
