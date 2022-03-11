import sqlite3

connection = sqlite3.connect(":memory:")


def create_table():
    cursor = connection.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        synopsis TEXT
    )
    """
    )
    cursor.close()


def seed():
    list_book = [
        Book(
            title="Pride and Prejudice",
            author="Jane Austen",
            synopsis="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        ),
        Book(
            title="Persuasion",
            author="Jane Austen",
            synopsis="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        ),
        Book(
            title="Gun, Germs, and Steel",
            author="Jared Diamond",
            synopsis="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        ),
    ]

    for book in list_book:
        book.save()


class Book:
    def __init__(
        self, id_number: int = -1, title: str = "", author: str = "", synopsis: str = ""
    ):
        self.id_number = id_number
        self.title = title
        self.author = author
        self.synopsis = synopsis

    @staticmethod
    def __map(data: tuple):
        book = Book(
            data[0],
            data[1],
            data[2],
            data[3],
        )
        return book

    def __str__(self):
        return f"Id\t\t: {self.id_number}\nTitle\t\t: {self.title}\nAuthor\t\t: {self.author}\nSynopsis\t: {self.synopsis}"

    def save(self):
        cursor = connection.cursor()
        cursor.execute(
            f"""
        INSERT INTO books(title, author, synopsis) VALUES('{self.title}', '{self.author}', '{self.synopsis}')
        """
        )
        connection.commit()
        cursor.close()

    @staticmethod
    def get(id: int):
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM books WHERE id={id}")
        book = Book.__map(cursor.fetchone())
        cursor.close()
        return book

    @staticmethod
    def get_all():
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM books")
        list_book = []

        for data in cursor.fetchall():
            list_book.append(Book.__map(data))
        return list_book


create_table()
seed()

list_book = Book.get_all()

for book in list_book:
    print(book)
    print()
