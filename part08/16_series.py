def minimum_grade(rating: float, series_list: list):
    result = []
    for series in series_list:
        if min(series.ratings) >= rating:
            result.append(series)
    return result


def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        for g in series.genres:
            if g == genre:
                result.append(series)
    return result



class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        header = f'{self.title} ({self.seasons} seasons)\n'
        genres_list = f'genres: {", ".join(self.genres)}\n'
        if len(self.ratings) == 0:
            ratings = 'no ratings'
        else:
            sum_ratings = sum(self.ratings)
            avg_ratings = sum_ratings / len(self.ratings)
            ratings = f'{len(self.ratings)} ratings, average {avg_ratings:.1f} points'
        return header + genres_list + ratings
    
    def rate(self, rating: int):
        self.ratings.append(rating)





if __name__ == '__main__':

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)