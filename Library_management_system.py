class library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def addbook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def show_details(self):
        print("Total number of books are {}".format(self.no_of_books))
        for book in self.books:
            print(book)

L1 = library()

L1.addbook("Harrypotter")
L1.addbook("Game of Thrones")
L1.show_details()