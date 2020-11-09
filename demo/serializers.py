from rest_framework import serializers
from .models import Book, BookFields


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            BookFields.ID.value,
            BookFields.TITLE.value,
            BookFields.DESCRIPTION.value,
            BookFields.PRICE.value,
            BookFields.PUBLISHED.value,
            BookFields.IS_PUBLISHED.value,
        ]
