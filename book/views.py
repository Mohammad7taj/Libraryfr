from django.shortcuts import render, HttpResponse , redirect
from book.models import Author , Book
from book.form import CategoryForm, AuthorForm

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

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            n = data.get('name')
            d = data.get('description')
            return redirect("home")
    form = CategoryForm()

    return render(request, 'book/new_category.html', context= {'cat_form':form})




def create_author(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            print(new_author)
            return redirect("home")
    return render(request, 'book/new_author.html', {'form':form})

    

