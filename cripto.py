import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Function to calculate technical indicators
def calculate_indicators(data):
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()
    
    # RSI calculation
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD calculation
    short_ema = data['Close'].ewm(span=12, adjust=False).mean()
    long_ema = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = short_ema - long_ema
    data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    return data

# Fetch data for a list of cryptocurrencies
cryptos = ['BTC-USD', 'ETH-USD', 'BNB-USD']
crypto_data = {}

for crypto in cryptos:
    data = yf.download(crypto, period='6mo', interval='1d')
    data = calculate_indicators(data)
    crypto_data[crypto] = data

# Analyze indicators for downtrend and potential reversal
for crypto, data in crypto_data.items():
    latest = data.iloc[-1]
    if latest['Close'] < latest['50_MA'] and latest['RSI'] < 40 and latest['MACD'] > latest['Signal']:
        print(f"{crypto} is in a downtrend and may reverse soon. Current price: {latest['Close']}, 50-day MA: {latest['50_MA']}, RSI: {latest['RSI']}, MACD: {latest['MACD']}, Signal: {latest['Signal']}")
