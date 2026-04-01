import pandas as pd

# load stock data
df = pd.read_csv("Data/final_stock_data.csv")

print(df.columns)

# convert date
df["date"] = pd.to_datetime(df["date"])

# 1️⃣ Yearly Returns
returns = df.groupby("Ticker")["close"].agg(lambda x: x.iloc[-1]/x.iloc[0]-1).reset_index()
returns.columns = ["Ticker","yearly_return"]

returns.to_csv("yearly_returns.csv", index=False)


# 2️⃣ Monthly Returns
df["month"] = df["date"].dt.to_period("M")

monthly_returns = df.groupby(["Ticker","month"])["close"].agg(lambda x: x.iloc[-1]/x.iloc[0]-1).reset_index()

monthly_returns.to_csv("monthly_returns.csv", index=False)


# 3️⃣ Correlation Matrix
pivot = df.pivot(index="date", columns="Ticker", values="close")

corr = pivot.corr()

corr.to_csv("correlation_matrix.csv")

print("Power BI data files generated successfully")