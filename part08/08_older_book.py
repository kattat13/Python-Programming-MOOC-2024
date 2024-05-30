class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------
def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f'{book1.name} is older, it was published in {book1.year}')
    elif book1.year > book2.year:
        print(f'{book2.name} is older, it was published in {book2.year}')
    else:
        print(f'{book1.name} and {book2.name} were published in {book1.year}')


if __name__ == '__main__':
    book1 = Book('Seven Brothers', 'Aleksis Kivi', 'Novel', 1870)
    book2 = Book('The Egyptian', 'Mika Waltari', 'Novel', 1945)
    older_book(book1, book2)