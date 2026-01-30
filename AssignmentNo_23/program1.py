#BookStore Class


class BookStore:
    NoOfBooks = 0     # Class variable

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1   # Increment book count

    def Display(self):
        print(self.Name, "by", self.Author,
              ". No of books:", BookStore.NoOfBooks)


# Creating objects
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()
