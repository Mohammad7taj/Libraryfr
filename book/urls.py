from django.urls import path
from book.views import home, index , book_detale, create_book 


urlpatterns = [
    path("list/", home, name='home'),
    path("", index, name='a'),
    path("detale/<id>/", book_detale, name='book'),
    path("book/new", create_book, name= 'creat'),


]





