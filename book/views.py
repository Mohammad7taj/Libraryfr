from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("helllllllo")


def home(request):
    return render(request, 'book/booklist.html')


