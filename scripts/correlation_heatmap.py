import pandas as pd
import matplotlib.pyplot as plt

# load stock data
df = pd.read_csv("stock_prices.csv")

# pivot table (dates as rows, tickers as columns)
pivot = df.pivot(index="date", columns="ticker", values="close")

# correlation matrix
corr = pivot.corr()

# plot heatmap
plt.imshow(corr)

plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Stock Price Correlation Heatmap")

plt.tight_layout()
plt.show()