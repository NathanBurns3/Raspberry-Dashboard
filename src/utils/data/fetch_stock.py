import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()

def fetch_stock():
    required_stocks = ["DGRO", "VFIAX"]
    other_stocks = ["AAPL", "GOOGL", "AMZN", "MSFT", "NVDA", "TSLA", "META", "NFLX"]
    random_stocks = random.sample(other_stocks, 4)
    all_stocks = required_stocks + random_stocks
    stocks_string = ",".join(all_stocks)
    api_key = os.getenv('STOCK_API_KEY')
    api_url = f"https://api.twelvedata.com/time_series?symbol={stocks_string}&interval=1day&outputsize=2&apikey={api_key}"
    response = requests.get(api_url)
    data = response.json()
    
    stocks = []
    for stock_data in data.values():
        if stock_data['status'] == 'ok':
            current_stock_values = stock_data['values'][0]
            previous_stock_values = stock_data['values'][1]
            current_price = round(float(current_stock_values['close']), 2)
            previous_close_price = round(float(previous_stock_values['close']), 2)
            percentage_change = round(((current_price - previous_close_price) / previous_close_price) * 100, 2)
            stocks.append({
                'name': stock_data['meta']['symbol'],
                'price': current_price,
                'percentage_change': percentage_change
            })
    
    return stocks