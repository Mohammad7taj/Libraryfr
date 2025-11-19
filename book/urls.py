from django.urls import path
from book.views import home, index , book_detale


urlpatterns = [
    path("", index, name='a'),
    path("lil/", home, name='d'),
    path("detale/<x>/", book_detale, name='s'),
]




