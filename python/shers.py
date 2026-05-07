import yfinance as yf
import pandas as pd

# Enter stock symbol (Example: Reliance Industries on NSE -> "RELIANCE.NS")
symbol = "RELIANCE.NS"

# Fetch stock data from listing to current date
stock = yf.Ticker(symbol)

# Get historical data from listing date
data = stock.history(period="max")   # "max" = full history

# Select required columns: Open, High, Low, Close, Volume
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Reset index to show Date as a normal column
data = data.reset_index()

# Display first 10 rows in console
print(data.head(10))

# Save to CSV file
file_name = f"{symbol}_stock_data.csv"
data.to_csv(file_name, index=False)
print(f"\n✅ Data saved to {file_name}")
