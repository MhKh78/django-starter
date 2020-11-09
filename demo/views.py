from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.


# class Another(View):
#     books = Book.objects.all()
#     output = ''

#     for book in books:
#         output += f"We have {book.description} many books in DB<br>"

#     def get(self, request):

#         return HttpResponse(self.output)


def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'books': books})
