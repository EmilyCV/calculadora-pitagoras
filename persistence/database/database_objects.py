# import sqlite3

# # Conectando
# conn = sqlite3.connect('database.db', check_same_thread=False)

# # Definindo um cursor
# cursor = conn.cursor()


# def create_db():
#     cursor.execute(f"""
#     CREATE TABLE user (
#     email TEXT NOT NULL
#                PRIMARY KEY,
#     nome  TEXT NOT NULL
# );
# CREATE TABLE catetos (
#     id              INTEGER NOT NULL
#                             PRIMARY KEY AUTOINCREMENT,
#     catetoOposto    NUMERIC NOT NULL,
#     catetoAdjacente NUMERIC NOT NULL,
#     resultado       NUMERIC NOT NULL,
#     email           STRING  NOT NULL,
#     FOREIGN KEY (
#         email
#     )
#     REFERENCES user (email)
# );
#     """)


# def create_user(email, name):
#     with sqlite3.connect('database.db') as con:
#         cursor.execute(
#             "INSERT INTO user (email,nome) VALUES (?,?)", (email, name))
#         cursor.execute('COMMIT')
#         msg = "Done"
#         # conn.close()


# def create_catetos(cateto_oposto, cateto_adjacente, resultado, email):
#     with sqlite3.connect('database.db') as con:
#         cursor.execute(
#             "INSERT INTO catetos (catetoOposto,catetoAdjacente,resultado,email) VALUES (?,?,?,?)", (cateto_oposto, cateto_adjacente, resultado, email))
#         cursor.execute('COMMIT')
#         msg = "Done"
#         conn.close()


# # Fechando conexão
# # conn.close()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

Base = declarative_base()


class Users(Base):
    # __tablename__ indica como sua tabela será realmente chamada dentro do banco de dados
    __tablename__ = 'user'
    email = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    def __init__(self,
                 email=str,
                 name=str
                 ):
        self.email = email
        self.name = name
    # __repr__ que será um texto que deve ser retornado quando tivermos a instância da classe User

    def __repr__(self):
        return f'User {self.name}'


class Catetos(Base):
    __tablename__ = 'catetos'
    id = (Column(Integer, primary_key=True, autoincrement=True))
    catetoOposto = Column(Float, nullable=False)
    catetoAdjacente = Column(Float, nullable=False)
    resultado = Column(Float, nullable=False)
    email = Column(String, ForeignKey('user.email'))

    def __init__(self,
                 id=int,
                 catetoOposto=float,
                 catetoAdjacente=float,
                 resultado=float,
                 email=None
                 ):
        self.id = id
        self.catetoOposto = catetoOposto
        self.catetoAdjacente = catetoAdjacente
        self.resultado = resultado
        self.email = email
