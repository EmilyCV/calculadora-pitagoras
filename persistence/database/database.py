from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from persistence.database.database_objects import Base

# engine é para ser a ponte de conexão entre o Python e o banco
engine = create_engine('sqlite:///database.db', echo=False, connect_args={"check_same_thread": False})

# uma 'session' para fazer um meio de campo entre os objetos que criamos no Python 
# e o engine que realmente se comunica com o banco de dados

# 'sessionmaker' pra passar o engine pra nossa sessão atual e criarmos de fato a sessão
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)