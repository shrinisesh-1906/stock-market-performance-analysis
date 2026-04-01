import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("stock_prices.csv")

# convert date
df["date"] = pd.to_datetime(df["date"])

# create month column
df["month"] = df["date"].dt.to_period("M")

# calculate monthly return
monthly = df.groupby(["ticker","month"])["close"].agg(
    lambda x: x.iloc[-1]/x.iloc[0]-1
).reset_index()

# loop through each month
months = monthly["month"].unique()

for m in months:

    data = monthly[monthly["month"] == m]

    gainers = data.sort_values("close", ascending=False).head(5)
    losers = data.sort_values("close").head(5)

    plt.figure(figsize=(10,5))

    plt.bar(gainers["ticker"], gainers["close"])
    plt.title(f"Top 5 Gainers - {m}")
    plt.show()

    plt.figure(figsize=(10,5))

    plt.bar(losers["ticker"], losers["close"])
    plt.title(f"Top 5 Losers - {m}")
    plt.show()