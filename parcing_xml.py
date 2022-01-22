# Разработайте поиск книги в библиотеке:
# по ее автору
# цене
# заголовку
# описанию

from xml.etree import ElementTree

tree = ElementTree.parse("library.xml")
root = tree.getroot()

library_dict = {}


def search_by_author(values):
    """Searhing books by author"""
    for book in root.iter("book"):
        title = book.find("title").text.split(".")
        author = book.find("author").text.split(".")
        doc1 = list(zip(title, author))
        library_dict.update(doc1)
    for k, v in library_dict.items():
        if v == values:
            print(k)


def search_by_price(values):
    """Searching books by their price"""
    for book in root.iter("book"):
        title = book.find("title").text.split(".")
        price = book.find("price").text.split()
        doc2 = dict(zip(title, price))
        library_dict.update(doc2)
    for k, v in library_dict.items():
        if v == values:
            print(k)


def search_by_title(values):
    """Searching id books by their title"""
    for book in root.iter("book"):
        title = book.find("title").text.split(".")
        book = book.attrib["id"].split()
        doc3 = dict(zip(book, title))
        library_dict.update(doc3)
    for k, v in library_dict.items():
        if v == values:
            print("Id book: ", k)


def search_by_description(value):
    """Searching books by their description"""
    for book in root.iter("book"):
        title = book.find("title").text.split(".")
        description = book.find("description").text.split(".")
        doc4 = dict(zip(title, description))
        library_dict.update(doc4)
    for k, v in library_dict.items():
        if v == value:
            print(k)


# Output title book by author "Gambardella, Matthew"
print(search_by_author("Gambardella, Matthew"))

# Output title book by price "7"
print(search_by_price("7"))

# Output id book by title "Clean Code"
print(search_by_title("Clean Code"))

# Output title book by description "A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and
# Code"
print(search_by_description("A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code"))
