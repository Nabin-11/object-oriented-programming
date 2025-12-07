print("*" * 10)
import csv


class Library:
    # class variable
    books_collection = []
    total_books = len(books_collection)

    def __init__(self, name, code: int, quantity=0):
        # assert to check the quantity is non negative
        assert quantity >= 0, "Quantity cannot be negative"

        # instance variables
        self.name = name
        self.code = code
        self.quantity = quantity

        Library.books_collection.append(self)
    
        def __repr__(self):
        # __repr__ should return a single-line, unambiguous representation
         return f"Library('{self.name}', {self.code}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        
        with open("Data.csv", 'r') as f:
            reader = csv.DictReader(f)
            lists = list(reader)
    
        for items in lists:
            print(items)




# Examples (commented out):
# book1 = Library("Python Programming", 101, 5)
# book2 = Library("Data Science", 102, 3)
# book3 = Library("Machine Learning", 103, 7)


Library.instantiate_from_csv()
# print(Library.books_collection)

print("*" * 10)