year = 2023

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



Book.books_info()
Book.calculation()