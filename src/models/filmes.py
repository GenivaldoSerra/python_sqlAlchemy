from src.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Filmes(Base):
    __tablename__ = 'filmes'
    
    titulo = Column(String(50), primary_key=True)
    genero = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f'Filme(titulo={self.titulo}, genero={self.genero}, ano={self.ano})'