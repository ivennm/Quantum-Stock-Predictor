import yfinance as yf
import pandas as pd



def get_data(ticker):
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period='1mo', interval='1d')

    data_html = historical_data[['Open', 'High', 'Low', 'Close', 'Volume']].to_html()
    financials = stock.financials.to_html()
    actions = stock.actions.to_html()

    return data_html, financials, actions
