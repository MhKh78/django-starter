from django.contrib.admin import ModelAdmin, register, site
from .models import Book, BookNumber, BookFields

# Register your models here.
# admin.site.register(Book)


@register(Book)
class BookAdmin(ModelAdmin):
    list_display = [
        BookFields.TITLE.value,
        BookFields.DESCRIPTION.value,
        BookFields.PRICE.value,
    ]
    fields = [
        BookFields.TITLE.value,
        BookFields.DESCRIPTION.value,
        BookFields.NUMBER.value,
    ]
    list_filter = [BookFields.PUBLISHED.value]
    search_fields = [BookFields.TITLE.value, BookFields.DESCRIPTION.value]


site.register(BookNumber)