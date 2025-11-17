from django.urls import path
from book.views import home, index


urlpatterns = [
    path('lil/', home),
    path("", index)

]



