import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("stock_prices.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["ticker", "date"])

# Calculate daily returns
df["daily_return"] = df.groupby("ticker")["close"].pct_change()

# Calculate volatility (standard deviation)
volatility = df.groupby("ticker")["daily_return"].std()

# Top 10 most volatile stocks
top10 = volatility.sort_values(ascending=False).head(10)

print(top10)

# Plot
top10.plot(kind="bar")
plt.title("Top 10 Most Volatile Stocks")
plt.xlabel("Stock Ticker")
plt.ylabel("Volatility (Std Dev of Daily Returns)")
plt.show()