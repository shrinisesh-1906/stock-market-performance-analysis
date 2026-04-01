import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("stock_prices.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["ticker","date"])

# Calculate daily returns
df["daily_return"] = df.groupby("ticker")["close"].pct_change()

# Calculate cumulative returns
df["cum_return"] = (1 + df["daily_return"]).groupby(df["ticker"]).cumprod() - 1

# Get final cumulative return for each stock
final_returns = df.groupby("ticker")["cum_return"].last()

# Select top 5 stocks
top5 = final_returns.sort_values(ascending=False).head(5).index

# Plot
plt.figure(figsize=(10,6))

for stock in top5:
    stock_data = df[df["ticker"] == stock]
    plt.plot(stock_data["date"], stock_data["cum_return"], label=stock)

plt.title("Cumulative Return of Top 5 Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()

plt.show()