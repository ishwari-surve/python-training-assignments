class BookStore:
    NoOfBooks = 0   

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1   

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()
