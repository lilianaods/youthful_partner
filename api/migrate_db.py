from sqlalchemy import create_engine

from api.models.task import Base

DATABASE_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

async_engine = create_engine(
    DATABASE_URL,
    echo=True,
)

def reset_database():
    Base.metadata.drop_all(bind=async_engine)
    Base.metadata.create_all(bind=async_engine)

if __name__ == "__main__":
    reset_database()