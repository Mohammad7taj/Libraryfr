from django.urls import path
from book.views import home, index , book_detale, create_book, create_author, create_category


urlpatterns = [
    path("list/", home, name='home'),
    path("", index, name='a'),
    path("detale/<id>/", book_detale, name='book'),
    path("book/new", create_book, name= 'creat'),
    path("category/new", create_category, name= 'new_category'),
    path("author/new", create_author, name= 'new_author'),


]





