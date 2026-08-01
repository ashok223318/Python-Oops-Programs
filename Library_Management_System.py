class Library:
    
    def __init__(self,books):
        self.books = books
        
    def display_books(self):
            print("\nAvailable Books:")
            for book in self.books:
                print(book)
                
    def borrow_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(book,"Borrowed Successfully")
        else:
            print("Book is Not Available")
            
    def return_book(self,book):
        self.books.append(book)
        print(book,"Return Successfully")
        
books = ["Python","Java","C++","DBMS"]
library = Library(books)

while True:
    print("\n======= Library Menu =======")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        library.display_books()
        
    elif choice == 2:
        book = input("Enter Book Name: ")
        library.borrow_book(book)
        
    elif choice == 3:
        book = input("Enter Book Name: ")
        library.return_book(book)
        
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")                          