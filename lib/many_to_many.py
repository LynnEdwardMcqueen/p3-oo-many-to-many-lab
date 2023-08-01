from datetime import *
from operator import attrgetter

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
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        contracts = self.contracts()
        royalty_sum = 0
        for contract in contracts:
            royalty_sum += contract.royalties
        return(royalty_sum)

      


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


    @classmethod
    def contracts_by_date(cls):
        ret_list = Contract.all
        ret_list.sort(key = attrgetter("date") )
        return(ret_list)

