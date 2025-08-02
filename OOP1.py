class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages  # Private attribute for encapsulation

    def get_summary(self):
        return f"'{self.title}' by {self.author}, {self.__pages} pages."

    def read(self):
        return f"You start reading '{self.title}'."

class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def read(self):
        return f"You open the eBook '{self.title}' on your device. File size: {self.file_size}MB."

class AudioBook(Book):
    def __init__(self, title, author, pages, narrator):
        super().__init__(title, author, pages)
        self.narrator = narrator

    def read(self):
        return f"You listen to '{self.title}' narrated by {self.narrator}."

physical = Book("1984", "George Orwell", 328)
ebook = EBook("Digital Fortress", "Dan Brown", 356, 5)
audiobook = AudioBook("Becoming", "Michelle Obama", 400, "Michelle Obama")

print(physical.get_summary())
print(physical.read())

print(ebook.get_summary())
print(ebook.read())

print(audiobook.get_summary())
print(audiobook.read())
