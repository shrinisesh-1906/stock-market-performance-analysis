import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_prices.csv")
sector = pd.read_csv("sector_data.csv")

# yearly return
returns = df.groupby("ticker")["close"].agg(lambda x: x.iloc[-1]/x.iloc[0]-1).reset_index()

# extract ticker from symbol column
sector["ticker"] = sector["Symbol"].str.split(":").str[1].str.strip()

# merge
merged = pd.merge(returns, sector, on="ticker")

# sector performance
sector_perf = merged.groupby("sector")["close"].mean()

# plot
sector_perf.plot(kind="bar")
plt.title("Average Yearly Return by Sector")
plt.ylabel("Return")
plt.show()