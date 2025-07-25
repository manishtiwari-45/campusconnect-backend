from sqlmodel import SQLModel, Session, create_engine
from app.core.config import DATABASE_URL

# The `connect_args` is needed only for SQLite
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session