class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        return f"{self.title} by {self.author} published in {self.year}"


my_book = Book("Noli Me Tangere", "Jose P. Rizal", 1951)
print(my_book.display_details())