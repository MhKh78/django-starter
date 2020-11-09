from django.contrib.admin import ModelAdmin, register
from .models import Book, BookFields

# Register your models here.
# admin.site.register(Book)


@register(Book)
class BookAdmin(ModelAdmin):
    list_display = [
        BookFields.TITLE.value,
        BookFields.DESCRIPTION.value,
        BookFields.PRICE.value,
    ]
    fields = [BookFields.TITLE.value, BookFields.DESCRIPTION.value]
    list_filter = [BookFields.PUBLISHED.value]
    search_fields = [BookFields.TITLE.value, BookFields.DESCRIPTION.value]
