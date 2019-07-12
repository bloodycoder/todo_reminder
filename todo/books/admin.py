from django.contrib import admin
from books.models import Publisher,Author,Book

# Create your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
