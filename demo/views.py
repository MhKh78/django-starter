from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.


# class Another(View):
#     books = Book.objects.all()
#     output = ''

#     for book in books:
#         output += f"We have {book.description} many books in DB<br>"

#     def get(self, request):

#         return HttpResponse(self.output)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
