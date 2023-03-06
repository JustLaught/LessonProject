from datetime import date
year = date.today().year

class Book:
    def __init__(self):
        self.name = input("Enter book name:  ")
        self.autor = input("Enter autor name:  ")
        self.year = int(input("Enter year of a book:  "))
# Create information print function
    def books_info(self):
        """Shows book information"""
        print(f'{self.name=}'
        f'Autor = {self.autor}\n'
        f'Year = {self.year}\n')

    def calculation(self):
        print(f'This book {year - self.year} year')


res = Book()
res.books_info()
res.calculation()