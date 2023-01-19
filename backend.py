# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:50:24 2023

@author: gabba
"""
from dotenv import load_dotenv
load_dotenv()

import os
import requests
from datetime import datetime, timedelta

# Replace YOUR_API_KEY with your actual API key
api_key = os.environ['API_KEY']

# Specify the stock symbol for the stock you want to look up
symbol = 'TSLA'

def get_current_value():
    # Make the API request to get the current value
    url_current = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response_current = requests.get(url_current)
    data_current = response_current.json()

    # Extract the current value of the stock from the API response
    current_value = data_current['Global Quote']['05. price']
    return current_value

def get_historical_values(start_date, end_date):
    # Make the API request to get the historical stock values
    url_historical = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=compact'
    response_historical = requests.get(url_historical)
    data_historical = response_historical.json()['Time Series (Daily)']

    # Extract the historical stock values within the given timerange
    historical_values = []
    for date, value in data_historical.items():
        if date >= start_date and date <= end_date:
            historical_values.append(
                {'date': date, 'value': float(value['4. close'])}
            )
    return historical_values

def get_default_timerange():
    # Get the current date
    now = datetime.now()

    # Default timerange for the historical stock values
    default_end_date = now.strftime("%Y-%m-%d")
    default_start_date = (now - timedelta(days=30)).strftime("%Y-%m-%d")
    return default_start_date, default_end_date