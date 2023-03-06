from src.data.filmes import FilmesDB


repo = FilmesDB()


data = repo.select()


print(data)