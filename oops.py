import csv
import os


class Book:
    discount = 0.8     # class attribute, every book shares this
    all = []           # every book object gets added here

    def __init__(self, title: str, copies: int, mrp: float = 100):

        # stop bad values before the object is even made
        assert copies >= 0, f"copies cant be negative, got {copies}"
        assert mrp >= 0, f"mrp cant be negative, got {mrp}"

        self.__title = title     # private, cant be accessed directly from outside
        self.copies = copies
        self.mrp = mrp

        Book.all.append(self)

    def stock_value(self):
        return self.copies * self.mrp

    def apply_discount(self):
        # self.discount checks the object first, if its not there it takes the class one
        self.mrp = self.mrp * self.discount

    # getter for the private title
    @property
    def title(self):
        return self.__title

    # setter so the title can still be changed, but only through this
    @title.setter
    def title(self, new_title):
        self.__title = new_title

    # abstraction - outside code just calls lend(), the checking part stays hidden
    def lend(self):
        if self.__in_stock():
            self.copies -= 1
            return f"{self.title} lent out, {self.copies} left"
        return f"{self.title} is out of stock"

    def __in_stock(self):
        return self.copies > 0

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}', {self.copies}, {self.mrp})"

    @classmethod
    def load_from_csv(cls):
        # so it finds the csv even if i run the file from some other folder
        path = os.path.join(os.path.dirname(__file__), "item.csv")
        with open(path, "r") as f:
            rows = list(csv.DictReader(f))
        for book in rows:
            cls(
                title=str(book.get("title")),
                copies=int(book.get("copies")),
                mrp=float(book.get("mrp"))
            )

    @staticmethod
    def is_whole_number(num):
        # 5.0 counts as whole, 5.5 doesnt
        if isinstance(num, float):
            return num.is_integer()
        if isinstance(num, int):
            return True
        return False


# inheritance - EBook gets everything from Book
class EBook(Book):
    all = []

    def __init__(self, title: str, copies: int, mrp: float = 100, size_mb: float = 2):
        super().__init__(title, copies, mrp)

        assert size_mb > 0, f"file size has to be more than 0, got {size_mb}"

        self.size_mb = size_mb
        EBook.all.append(self)


Book.load_from_csv()
print(Book.all)

ebook1 = EBook("Wings of Fire", 50, 199, 3.5)
print(EBook.all)
print(ebook1.stock_value())    # 9950

# class attribute vs instance attribute
ebook1.discount = 0.5          # only this ebook gets 50% off
ebook1.apply_discount()
print(ebook1.mrp)            # 99.5
print(Book.discount)           # still 0.8 for the rest

print(Book.is_whole_number(7.0))   # True

# encapsulation
book1 = Book("Ponniyin Selvan", 2, 450)
print(book1.title)
book1.title = "Ponniyin Selvan Part 1"
print(book1.title)
# print(book1.__title)  -> AttributeError, its private

print(book1.lend())
print(book1.lend())
print(book1.lend())
