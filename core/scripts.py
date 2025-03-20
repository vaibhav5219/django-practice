
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from datetime import datetime, timedelta
from django.db.models import Avg, Count, Min, Max, Count, Sum, Q, Subquery, OuterRef
import random
from home.models import Author, Book


def handel():

    # this is queryset
    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     published_date__year = 2023
    # ).order_by('-published_date').values('book_name')
    # authors = Author.objects.annotate(books = Subquery(book)) # this is subquery

    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     published_date__year = 2023
    # ).values('author').annotate(total_price = Sum('price')).values('total_price')
    # authors = Author.objects.annotate(total_price_for_book = Subquery(book)) # this is subquery

    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     published_date__year = 2023
    # ).values('author').annotate(book_count = Count('id')).values('book_count')
    # authors = Author.objects.annotate(book_count = Subquery(book)) # this is subquery

    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     published_date__year = 2023
    # ).values('author').annotate(book_price = Avg('price')).values('book_price')
    # authors = Author.objects.annotate(book_price = Subquery(book)) # this is subquery

    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     published_date__year = 2023,
    #     price__gte = 50,
    # ).values('author').order_by('-price').values('price')[:1]
    # authors = Author.objects.annotate(book_price = Subquery(book)) # this is subquery

    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     price__gte = 50,
    # ).values('author')[:1]
    # authors = Author.objects.annotate(id__in = Subquery(book.values('author'))) # this is subquery

    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     published_date__year__gte = 2023,
    # ).values('author').annotate(earning = Sum('price')).values('earning')
    # authors = Author.objects.annotate(total_earning = Subquery(book)) # this is subquery

    # book = Book.objects.filter(
    #     author = OuterRef('id'),
    #     published_date__year__gte = 2023,
    # ).values('author').annotate(book_price = Max('price')).values('book_price')
    # authors = Author.objects.annotate(book_price = Subquery(book)) # this is subquery

    book = Book.objects.filter(
        author = OuterRef('id'),
        published_date__year__gte = 2023,
    ).values('author').annotate(book_price = Max('price')).values('book_price')
    authors = Author.objects.annotate(book_price = Subquery(book)) # this is subquery

    for author in authors:
        # print(vars(author))
        # print(f"Author Name => {author.author_name} ")
        print(f"Author Name => {author.author_name}  and book => {author.book_price}")

handel()