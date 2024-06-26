from django.urls import path
from .views import (
    author_books,
    author_details,
    authors_list,
    book_details,
    books_list,
    books_with_tag,
    borrow_details,
    borrows_list
)

app_name="books"
urlpatterns = [
    path('books/', books_list, name="books_list"),
    path('books/tag/<str:tag>/', books_with_tag, name='books_with_tag'),
    path('book/<int:id>', book_details, name="book_details"),
    path('authors/', authors_list, name="authors_list"),
    path('author/<int:id>', author_details, name="author_details"),
    path('books/author/<str:name>', author_books, name="author_books"),
    path('borrows/<str:username>', borrows_list, name="borrows_list"),
    path('borrow/<int:id>', borrow_details, name="borrow_details"),
]