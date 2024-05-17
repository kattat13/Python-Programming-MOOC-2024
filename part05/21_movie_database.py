def add_movie(database: list, 
              name: str, 
              director: str, 
              year: int, 
              runtime: int):
    movie = {"name": name,
             "director": director,
             "year": year,
             "runtime": runtime}
    database.append(movie)
