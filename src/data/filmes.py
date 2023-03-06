from src.configs.connection import DBconnection
from src.models.filmes import Filmes


class FilmesDB:
    def select(self):
        with DBconnection() as db:
            data = db.session.query(Filmes).all()
            return data