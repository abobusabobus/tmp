from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
metadata = MetaData()

# ВАЖНО: импортируем модели, чтобы таблицы зарегистрировались в metadata
import models  # <-- здесь models.users добавится в metadata

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)  # создаёт таблицы, включая users
