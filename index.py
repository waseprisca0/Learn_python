def self_books(title,year):
    print(title, year)

    book = open("db.txt", "w")
    book.write(f"[{title},{year}]")
   
self_books("Rwanda nziza", "2004")

    
#write(f"[{title},{year}]")

    
