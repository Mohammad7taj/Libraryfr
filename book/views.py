from django.shortcuts import render, HttpResponse , redirect
from book.models import Author , Book


def index(request):
    return HttpResponse("helllllllo")


def home(request):
    data = Book.objects.all()
    context = {'books':data}
    return render(request, 'book/booklist.html', context)

def book_detale(request, id):
    book = Book.objects.filter(id=id).first()
    context = {'book':book}
    return render(request, 'book/bookdetale.html', context)


def create_book(request):
    if request.method == 'POST':
        titl = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        new_book = Book.objects.create(titl=titl, author=author, category=category)
        print(new_book)

        return redirect('home')
    else:
        return render(request, 'book/new_book.html')



