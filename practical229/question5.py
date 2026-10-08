class Book:

  def __init__(self, book_id, title, author, quantity):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.quantity = quantity
    self.is_available = quantity > 0

  def issue_book(self):
    if self.quantity > 0:
      self.quantity -= 1
      if self.quantity == 0:
        self.is_available = False
      print(f"Book '{self.title}' issued successfully.")
    else:
      print(f"Sorry, '{self.title}' is currently out of stock.")

  def return_book(self):
    self.quantity += 1
    self.is_available = True
    print(f"Book '{self.title}' returned successfully.")


# Example Usage:
my_book = Book(book_id="101", title="Python Programming", author="John Doe", quantity=2)

my_book.issue_book()  # Quantity becomes 1
my_book.return_book()  # Quantity becomes 2