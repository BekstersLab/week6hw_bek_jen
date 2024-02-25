from book_classes import Book
from book_classes import Magazine
from book_classes import get_all_info

# Object 1
dune_book = Book('Dune', 'Frank Herbert', 'Science Fiction')

info = dune_book.get_info()

print(info)

dune_book.set_start_date()

print(dune_book.get_start_date())

# Object 2
platform_book = Book('People on Platform 5', 'Clare Pooley', 'Fiction')

info2 = platform_book.get_info()

print(info2)

platform_book.set_start_date('2023', '01', '25')

start = platform_book.get_start_date()

platform_book.set_end_date()

end = platform_book.get_end_date()

# Object 3
time_out = Magazine('Time Out', 'Time Out Group', 10)

print(time_out.get_info())

length = dune_book - platform_book

print(length)

get_all_info(dune_book)
