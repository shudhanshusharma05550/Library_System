class Library():
    def __init__(self,list_of_books,name_of_the_library):
        self.list_of_books = list_of_books
        self.name_of_the_library = name_of_the_library
        self.lended_books = []

    def DisplayBook(self):
        for items in self.list_of_books:
            print(items)
        return "The books we provide from our Library"

    def AddBook(self,book):
        self.list_of_books.append(book)
        for items in self.list_of_books:
                print(items)

    def LendedBook(self,book_name):
        if book_name in self.list_of_books:
            self.lended_books.append(book_name)
            self.list_of_book.remove(book_name)
            print(f"lending of {self.book_name} is Under process.............\n")
            print("Congrats books lends for you\n")

        elif book_name not in self.list_of_books:
            print("This book is under lending process.....\n We left with--------\n")
            for items in self.list_of_books:
                print(items)

        else:
            print("name of the book you have entered is not available or might be wrong you entered .....")
            print("We left with-----\n")
            for items in self.list_of_books:
                print(items)

    def ReturnBook(self,name):
        self.list_of_books.append(name)
        for items in self.list_of_books:
            print(items)
        print("You have returned the book Successfully.........\n")


def LibSystem():
    flag = True
    Pathshala = Library(["Jab WE Met", "Junior G","Hello G","Sonpari","Shaktimaan"] ,"Pathshala Library")
    
    while flag == True:
        username = input("Enter your Good name \n")
        user_choice = int(input(f"Welcome to {username} in our {Pathshala.name_of_the_library}\n"
                                f"(1) for Display the books are available in Library \n"
                                f"(2) for Donate/Add the books \n"
                                f"(3) for Lend the book \n"
                                f"(4) for Return the Book \n"))

        if (user_choice == 1):
            print(Pathshala.DisplayBook())

        if (user_choice == 2):
            book = input("Enter the book name \n")
            print(Pathshala.AddBook(book))

        if (user_choice == 3):
            book_name = input("Enter the book name \n")
            print(Pathshala.LendedBook(book_name))

        if (user_choice == 4):
            name = input("Enter the name you returning\n")
            print(Pathshala.ReturnBook(name))

        else:
            print("Exit............")
        
        LibSystem()

LibSystem()