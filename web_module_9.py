import requests
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient

url = 'https://quotes.toscrape.com/'

def scrape_quotes():
    quotes = []
    authors = {}

    page_number = 1
    while True:
        response = requests.get(f'{url}/page/{page_number}/')
        soup = BeautifulSoup(response.text, 'html.parser')

        quote_elements = soup.select('.quote')
        if not quote_elements:
            break

        for quote_element in quote_elements:
            text = quote_element.select_one('.text').get_text()
            author = quote_element.select_one('.author').get_text()
            tags = [tag.get_text() for tag in quote_element.select('.tag')]

            quotes.append({
                'text': text,
                'author': author,
                'tags':tags
            })

            if author not in authors:
                authors[author] = {
                    'name':author,
                    'url': url + quote_element.select_one('small.author ~ a') ['href']
                }
        page_number += 1

    return quotes, authors

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    quotes, authors = scrape_quotes()
    save_to_json(quotes, 'quotes.json')
    save_to_json(authors, 'authors.json')

    print("Data successfully saved to quotes.json and authors.json")

    client = MongoClient('mongodb://localhost:27017/')
    db = client['quotes_db']  
    quotes_collection = db['quotes']  

    quotes_collection.insert_many(quotes)

    authors_collection = db['authors']
    authors_collection.insert_many([{'name': name, **info} for name, info in authors.items()])

    print("Data successfully saved to MongoDB")
    