from django.db import models
import enum

# Create your models here.


class BookFields(enum.Enum):
    TITLE = 'title'
    DESCRIPTION = 'description'
    PRICE = 'price'


class Book(models.Model):
    # BOOKS = (
    #     ('HB', 'Hobbit'),
    #     ('LOTR', 'Lord Of The Rings')
    # )
    title = models.CharField(
        max_length=36, blank=False, null=True, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    created = models.DateField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
