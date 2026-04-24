# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM) – sposób odwzorowania obiektowej architektury
# systemu informatycznego na bazę danych (lub inny element systemu) o relacyjnym charakterze.

# sqlalchemy - orm w pythonie
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# pip install sqlalchemy

engine = create_engine("sqlite:///test.db", echo=True)  # echo - logowanie bazy danych

# klasa bazowa
Base = declarative_base()


# model, encja - klasa odwzorowujaca tabelę w bazie danych
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# tworzenie tabeli w bazie danych
Base.metadata.create_all(bind=engine)
# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age INTEGER,
# 	PRIMARY KEY (id)
# )

# tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# doawanie rekordu
new_user = User(name="Jan", age=30)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)  ('Jan', 30)
session.commit()

# odczyt z bazy
users = session.query(User).all()
for user in users:
    print(f"User: {user.id}, {user.name}, {user.age}")
#
# User: 1, Jan, 30
# User: 2, Jan, 30
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
