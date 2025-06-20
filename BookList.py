class Book:
    def __init__(self, title, ISBN, author, price):
        self.__title = title
        self.__ISBN = ISBN
        self.__author = author
        self.__price = price

    def __str__(self):
        return f"Title: {self.__title}, \
ISBN: {self.__ISBN}, \
Author: {self.__author}, \
Price: ${self.__price:.2f}"

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def get_ISBN(self):
        return self.__ISBN

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

def create_book():
    title = input("Enter the book title: ")
    while True:
        ISBN = input("Enter the book ISBN (numbers only): ")
        if ISBN.isdigit():
            break
        else:
            print("ISBN must contain only numbers.")
    author = input("Enter the book author: ")
    while True:
        try:
            price = float(input("Enter the book price: "))
            if price >= 0:
                break
            else:
                print("Price cannot be negative.")
        except ValueError:
            print("Invalid price. Please enter a valid number.")
    return Book(title, ISBN, author, price)

def create_list_books():
    books = []
    while True:
        add_book = input("Do you want to add a new book? (yes/no): ").lower()
        if add_book == 'yes':
            book = create_book()
            books.append(book)
        elif add_book == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")
    return books

def find_book_price(books):
    try:
        price = float(input("Enter the price to search for books below this \
price: "))
        for book in books:
            if book.get_price() < price:
                print(book)
    except ValueError:
        print("Invalid price. Please enter a valid number.")

def find_book_ISBN(books):
    ISBN = input("Enter the ISBN to search for the book: ")
    for book in books:
        if book.get_ISBN() == ISBN:
            print(book)
            return
    print("Book not found.")

def main():
    books = create_list_books()
    while True:
        print("\nMenu:")
        print("1. Search by price")
        print("2. Search by ISBN")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            find_book_price(books)
        elif choice == '2':
            find_book_ISBN(books)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
