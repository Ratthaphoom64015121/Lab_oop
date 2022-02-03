class Book:
    BookNum = 0
    def __init__(self,ISNB,Authors,Title,Subject,DDSnumber):
       self.ISNB = ISNB
       self.authors = Authors.name
       self.title = Title
       self.subject = Subject
       self.DDSnumber = DDSnumber
       Book.BookNum += 1

    def ShowInFo(self):
        Info = [self.ISNB,self.authors,self.title,self.subject,self.DDSnumber]
        Title = ["ISNB : ","Authors : ","Title : ","Subject : ","DDS Number : "]
        for e in range(Book.BookNum) :
            print("\n"+str(e+1)+". ")
            for i,InfoBook in enumerate(Info):
                print("     "+Title[i] + str(InfoBook))

class Author:
    def __init__(self,Name):
        self._name = Name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,NewName):
        if isinstance(NewName,str):
            self.name = NewName
        else:
            print("No Number allowed")



class Catalog:
    def __init__(self,Book):
        self.catalog = Book
    def SearchTitle(self,Title):
        for Catalog in self.catalog:
            if Catalog.title == Title :
                Catalog.ShowInFo()
            else:
                print("Did not find this book!!!")

    def SearchISBN(self,ISBN):
        for Catalog in self.catalog:
            if Catalog.ISNB == ISBN :
                Catalog.ShowInFo()
            else:
                print("Did not find this book!!!")
    def SearchDDS(self,DDS):
        for Catalog in self.catalog:
            if Catalog.DDSnumber == DDS:
                Catalog.ShowInFo()
            else:
                print("Did not find this book!!!")
    def SearchAuthor(self,Authors):
        for Catalog in self.catalog:
            if Authors in Catalog.authors:
                Catalog.ShowInFo()
            else:
                print("Did not find this book!!!")
    def ShowBook(self):
        for Catalog in self.catalog:
                Catalog.ShowInFo()


AuthorName = []
BookCatalog = []


def addbook():
    NotFound  = 0
    NameArt = input("\nAuthor : ")
    if NameArt.isdigit()==True:
        print("Please enter a valid value")
    else:
        if len(AuthorName) == 0:
            AuthorName.append(Author(NameArt))
            # NameFales = int(input("แก้ชือกด 1 : "))
            # if NameFales == 1:
            #     NameArt = str(input("ชื่อผู้แต่ง : "))
            #     AuthorName[len(AuthorName) - 1].name = NameArt
            NameBook = input("Title : ")
            ISNB =  input("ISBN : ")
            Subject = input("Subject : ")
            DDSnumber = input("DDS Number : ")
            if ISNB.isdigit() and DDSnumber.isdigit():
                BookCatalog.append(Book(ISNB, AuthorName[0], NameBook, Subject ,DDSnumber))
            else:
                print("\n Please enter a valid value")

        else:
            NotFoundBook = 0
            for Name in AuthorName:
                if Name.name == NameArt:
                    NameBook = input("Title : ")
                    if len(BookCatalog) == 0:
                        ISNB =  input("ISBN : ")
                        Subject = input("Subject : ")
                        DDSnumber = input("DDS Number : ")
                        if ISNB.isdigit() and DDSnumber.isdigit():
                            BookCatalog.append(Book(ISNB, Name,NameBook,Subject,DDSnumber))
                    else:
                        for BookCat in BookCatalog:
                            if BookCat.title != NameBook:
                                NotFoundBook += 1
                        if NotFoundBook == len(BookCatalog):
                            ISNB =  input("ISBN : ")
                            Subject = input("Subject : ")
                            DDSnumber = input("DDS Number : ")
                            if ISNB.isdigit() and DDSnumber.isdigit():
                                BookCatalog.append(Book(ISNB, Name, NameBook, Subject,DDSnumber))
                elif Name.name != NameArt:
                    NotFound += 1
            if NotFound == len(AuthorName):
                AuthorName.append(Author(NameArt))
                if AuthorName == NameArt:
                    NameArt = str(input("Author : "))
                    AuthorName[len(AuthorName) - 1].name = NameArt
                NameBook = input("Title : ")
                ISNB =  input("ISBN : ")
                Subject = input("Subject : ")
                DDSnumber = input("DDS Number : ")
                BookCatalog.append(Book(ISNB, AuthorName[len(AuthorName)-1], NameBook, Subject,DDSnumber))

def Option_Search(select):
    BookSearch = Catalog(BookCatalog)
    if select == 1:
        BookSearch.SearchTitle(str(input("\nTitle : ")))
    if select == 2:
        BookSearch.SearchISBN(int(input("\nISBN : ")))
    if select == 3:
        BookSearch.SearchDDS(int(input("\nDDS numer : ")))
    if select == 4:
        BookSearch.SearchAuthor(str(input("\nAuthor : ")))


while True:
    print("\n   Select Option \n")
    Option = int(input("1.AddBook , 2.Search Book , 3.Delete Book : "))
    if Option == 1:
        addbook()

    if Option == 2:
        print("Search Form \n")
        select = int(input("      1.Title , 2.ISBN , 3.DDS Number, 4.Author : "))
        Option_Search(select)
        
    elif Option == 3:
        DelBook = Catalog(BookCatalog)
        DelBook.ShowBook()
        BookName = input("\nRemove Book Title : ")
        for i,BookDel in enumerate(BookCatalog):
            if BookDel.title == BookName:
                BookCatalog.pop(i)
                print("Remove Book Successfully.")
                break


