from datetime import *

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        ret_list = [contract for contract in Contract.all if contract.author == self]
        return ret_list

    def books(self):
        ret_list = self.contracts()
        return_book_list = []
        for ret_obj in ret_list:
            if ret_obj.author == self:
                return_book_list.append(ret_obj.book)
        return return_book_list


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        ret_list = [contract for contract in Contract.all if contract.book == self]
        return ret_list
    
    def authors(self):
        ret_contract = self.contracts()
        return [ret_contract[0].author]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties = None):
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("book not a Book instance")

        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("author not an Author instance")
    
        self.date = date

        if (type(royalties) == int):
            self.royalties = royalties
        else:
            raise Exception("royalties must an integer")
        
        Contract.all.append(self)
    
    @property
    def date(self):
        date_time = self._date.strftime("%m/%d/%Y")
        return date_time
    
    @date.setter
    def date(self, date):
        self._date = datetime.strptime(date, '%m/%d/%Y')

author1 = Author("Rosetta Stone")
book1 = Book("One Flew Over the PooPoo Chair")
contract1 = Contract(author1, book1 , '01/02/2003', 50000)
               
book2 = Book("Hands on Assets")
contract2 = Contract(author1, book2, "02/03/2004", 1000 )

book3 = Book("A Willing Volunteer")
author2 = Author("Linda Anderson")
contract3 = Contract(author2, book3, "03/04/2005", 80000)

contracts = author1.contracts()
for contract in contracts:
    print(contract.book.title)



contracts2 = author2.contracts()
for contract in contracts2:
    print(contract.book.title)

author1books = author1.books()
print("Author1 books")
for book in author1books:
    print(book.title)

contracts = book1.contracts()
print("Book contracts")
for contract in contracts:
    print(contract.book.title)

authors = book1.authors()
print("Book Authors")
print(authors[0].name)



