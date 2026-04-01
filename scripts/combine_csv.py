import pandas as pd
import os

folder = "Data/Transformed Data"

all_data = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path)
        df["Ticker"] = file.replace(".csv","")
        all_data.append(df)

final_df = pd.concat(all_data)

final_df.to_csv("Data/final_stock_data.csv", index=False)

print("Combined dataset created!")