from django.shortcuts import render, HttpResponse
from book.models import Author , Book


def index(request):
    return HttpResponse("helllllllo")


def home(request):
    data = Book.objects.all()
    context = {'har':data}
    return render(request, 'book/booklist.html', context)

def book_detale(request, x):
    book = Book.objects.filter(id=x).first()
    context = {'book':book}
    return render(request, 'book/bookdetale.html', context)

