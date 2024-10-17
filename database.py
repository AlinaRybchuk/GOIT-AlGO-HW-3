from mongoengine import Document, StringField, ReferenceField, connect
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# Підключення до бази даних MongoDB
connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

# Модель для авторів
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

# Модель для цитат
class Quote(Document):
    tags = StringField(required=True)
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)

def load_authors(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        authors = json.load(f)
        for author_data in authors:
            author = Author(
                fullname=author_data['fullname'],
                born_date=author_data['born_date'],
                born_location=author_data['born_location'],
                description=author_data['description']
            )
            author.save()
            print(f"Saved author: {author.fullname}")

def load_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        quotes = json.load(f)
        for quote_data in quotes:
            author = Author.objects(fullname=quote_data['author']).first()
            if author:
                quote = Quote(
                    tags=quote_data['tags'],
                    author=author,
                    quote=quote_data['quote']
                )
                quote.save()
                print(f"Saved quote: {quote.quote} by {author.fullname}")
            else:
                print(f"Author not found for quote: {quote_data['quote']}")

if __name__ == "__main__":
    connect('authors_database')

    load_authors('authors.json')
    load_quotes('quotes.json')