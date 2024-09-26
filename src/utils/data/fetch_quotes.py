import requests
import json
from models.quotes import Quote
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_quotes():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    api_key = os.getenv('QUOTE_API_KEY')
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        quote_data = json.loads(response.text)
        item = quote_data[0]
        quote = {
            'quote': item['quote'],
            'author': item['author']
        }
        return quote
    else:
        print("Error:", response.status_code, response.text)