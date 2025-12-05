
print("*"*50)


class Library:
 #class variable
    books_collection = []
    totoal_books =len( books_collection)

    def __init__(self, name,code:int,quantity=0):
        
        #assert to check the quantity is non negative
        assert quantity >= 0, "Quantity cannot be negative"

        #there all are instance variable ( instance means obect so instance variable means object variable)
        self.name = name
        self.code = code
        self.quantity = quantity

        Library.books_collection.append(self)
    # using repr to list all the books. 
    def __repr__(self):
        return f"""
Book          : {self.name}
Book code     : {self.code}
Book quantity : {self.quantity}

"""
        

book1 = Library("Python Programming", 101, 5)
book2 = Library("Data Science", 102, 3)
book3 = Library("Machine Learning", 103, 7)



print(repr(Library.books_collection))