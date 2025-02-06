import yfinance as yf
import pandas as pd



def get_data(ticker):
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period='1mo', interval='1d')        

    with open(f"{ticker}_stock_data.txt", 'w') as f:

        f.write(f"{ticker} Stock Data for the Last Month:\n")
        f.write(historical_data[['Open', 'High', 'Low', 'Close', 'Volume']].to_string())
        f.write("\n\n")

        f.write(f"Financials:\n{stock.financials.to_string()}\n\n")

        f.write(f"Stock Actions:\n{stock.actions.to_string()}")

    print(f"Data written to {ticker}_stock_data.txt")


if __name__ == "__main__":
    stock_name = input('stock name:')
    data = get_data(stock_name)
    