# class Book:
#     def __init__(self,author,title,year):
#         self.title=title
#         self.author=author
#         self.year=year
#
#     def __str__(self):
#         return f"{self.title} by {self.author} in {self.year}"
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Book {book.title} duoc them vao thu vien.")
#
#
#     def find_book(self, title):
#         for book in self.books:
#             if book.title.lower() in title.lower():
#                 return f"Có sách {title} trong thư viện"
#         else:
#             print("Không có sách")
#
#     def display_books(self):
#         if not self.books:
#             print("khong tim thay sach")
#         else:
#             print("Thu vien da co sach nay")
#             for book in self.books:
#                 print(book)
#
#
# # Tạo một số cuốn sách
# book1 = Book("Son", "vit", 2022)
# book2 = Book("Ronaldo", "the gioi", 2025)
# book3 = Book("Messi", "the thao", 2008)
#
# # Tạo một thư viện và thêm các cuốn sách vào đó
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Hiển thị danh sách sách trong thư viện
# library.display_books()
#
# # Tìm kiếm sách theo tên
# search_book = "viet nam"
# found_book = library.find_book(search_book)
# if found_book:
#     print(f"Sach: {found_book} co trong thu vien")
# else:
#     print(f"Khong tim thay sach '{search_book}' trong thu vien.")
#
#
#
#
#
#
#
#
#
