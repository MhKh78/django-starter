from rest_framework import serializers
from .models import (
    Book,
    BookNumber,
    BookFields,
    Character,
    CharacterFields,
    BookNumberFields,
)


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = [
            BookNumberFields.ID.value,
            BookNumberFields.ISBN_10.value,
            BookNumberFields.ISBN_13.value,
        ]


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [CharacterFields.BOOK.value, CharacterFields.NAME.value]


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            BookFields.ID.value,
            BookFields.TITLE.value,
            BookFields.DESCRIPTION.value,
            BookFields.PRICE.value,
            BookFields.PUBLISHED.value,
            BookFields.IS_PUBLISHED.value,
            BookFields.NUMBER.value,
            BookFields.CHARACTERS.value,
        ]
