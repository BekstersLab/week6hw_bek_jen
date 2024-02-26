from book_classes import Book
from book_classes import Chapter

# Object 1
dune_book = Book('Dune', 'Frank Herbert', 'Science Fiction')
# Object 2
platform_book = Chapter('People on Platform 5', 'Clare Pooley', 'Fiction', 384)

dune_book.set_start_date(12, 5, 2023)
dune_book.set_end_date(22,8, 2023)
print(dune_book, '\n')

platform_book.set_start_date(29, 9, 2023)
platform_book.set_end_date()
print(platform_book, '\n')

platform_book.add_pages(150)
platform_book.get_pages_info()
