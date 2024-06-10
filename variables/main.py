from library import Book, Library

def main():
    library = Library()

    book1 = Book("The Catcher in the Jungle", "Prisca", "123456789")
    book2 = Book("Rwanda Nziza", "Kevin", "987654321")

    print(library.add_book(book1))
    print(library.add_book(book2))

    print(library.check_out_book("The Catcher in the Jungle"))
    print(library.check_out_book("The Catcher in the Jungle"))

    print(library.return_book("The Catcher in the Jungle"))
    print(library.return_book("The Catcher in the Jungle"))

    print(library.check_out_book("Cars in Rwanda"))
    
if __name__ == "__main__":
    main()
