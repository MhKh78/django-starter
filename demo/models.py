from django.db import models
import enum

# Create your models here.


class BookFields(enum.Enum):
    ID = "id"
    TITLE = "title"
    DESCRIPTION = "description"
    PRICE = "price"
    PUBLISHED = "published"
    IS_PUBLISHED = "is_published"
    NUMBER = "number"


class BookNumberFields(enum.Enum):
    ID = "id"
    ISBN_10 = "isbn_10"
    ISBN_13 = "isbn_13"


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True, unique=True)
    isbn_13 = models.CharField(max_length=13, blank=True, unique=True)

    def __str__(self):
        return f"Book Number {self.isbn_10}"


class Book(models.Model):
    # BOOKS = (
    #     ('HB', 'Hobbit'),
    #     ('LOTR', 'Lord Of The Rings')
    # )
    title = models.CharField(max_length=36, blank=False, null=True, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="covers/", blank=True)
    created = models.DateField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    number = models.OneToOneField(
        BookNumber, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
