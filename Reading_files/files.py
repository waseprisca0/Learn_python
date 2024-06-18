import json

class Book:
    def __init__(self, title, author, isbn):


        self.title = title
        self.author = author
        self.isbn = isbn



    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }
    
    def from_dict(book_dict):
        return Book(book_dict['title'], book_dict['author'], book_dict['isbn'])
    
class Library:
    
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    #def view_books(self):
        #if not self.books:
            #print("No books in the library.")
        #else:
            #for book in self.books:
                #print(book)

    def save_to_file(self, filename):
        
        
        for book in self.books:
            print({book.title},{book.author},{book.isbn})
            with open(filename, 'a') as file:
                file.write(( json.dumps({'title': book.title, 'author': book.author, 'isbn': book.isbn}) + '\n'))

        
        print(f"Library data saved to {filename}.")
       

    def load_books(self):
        with open("data.txt", "r") as contents:
            for book in contents:
                print(book)

    def search_book(self, search_title):
        found_books = [book for book in self.books if search_title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No books found with title '{search_title}'.")

def main():

    #title = str(input("enter title: \n"))
    #author= str(input("enter author: \n"))
    #isbn = str(input("enter isbn: \n"))

    #book= Book(title,author,isbn)
    # Create a library instance and add some books
    library = Library()
    #book1 = Book("Health first", "Prisca M", "S123456789")
    #book2 = Book("How to get money", "Uwase P", "P987654321")
    #library.add_book(book)
    #library.add_book(book1)
    #library.add_book(book2)

    # View books in the library
    #print("\nBooks in the library:")
    #library.view_books()

    # Save the library to a file
    #library.save_to_file('data.txt')
    #library.load_books()

    while True:
        print("\n######## Welcome to the Library ###############")
        print("1. View all books")
        print("2. Search a book")
        print("3. Add a book")
        print("4. Check out a book")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            library.load_books()
        elif choice == '2':
            search_title = input("Enter the title of the book to search: ")
            library.search_book(search_title)
        elif choice == '3':
            while True:
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book = Book(title, author, isbn)
                library.add_book(book)
                more = input("Add another book? (y/n): ")
                if more.lower() != 'y':
                    break
        elif choice == '4':
            print("Check-out functionality is not implemented yet.")
        elif choice == '5':
            library.save_to_file('data.txt')
            break
        else:
            print("Invalid choice. Please try again.")
    


if __name__ == "__main__":
    main()