import os
import django
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


from home.models import Author, Book


# Initialize Faker
fake = Faker()

def create_authors(n=10):
    """Create n fake authors"""
    authors = []
    for _ in range(n):
        author = Author.objects.create(author_name=fake.name())
        authors.append(author)
    return authors

def create_books(authors, n=50):
    """Create n fake books linked to random authors"""
    for _ in range(n):
        author = random.choice(authors)  # Randomly select an author
        book_name = fake.sentence(nb_words=3)  # Generate a book title
        published_date = fake.date_between(start_date="-10y", end_date="today")  # Date within last 10 years
        price = round(random.uniform(100, 1000), 2)  # Generate random price between 100-1000
        
        Book.objects.create(
            author=author,
            book_name=book_name,
            published_date=published_date,
            price=price
        )

def populate_database():
    print("Creating authors...")
    authors = create_authors(10)  # Creates 10 authors
    print("Creating books...")
    create_books(authors, 50)  # Creates 50 books
    print("Fake data insertion complete!")

if __name__ == "__main__":
    populate_database()
