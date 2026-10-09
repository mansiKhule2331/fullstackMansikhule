class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


# Create an object
b1 = Book("Python Programming", "John Smith", 450)

# Display book information
b1.display()