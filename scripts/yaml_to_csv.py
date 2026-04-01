import os
import yaml
import pandas as pd

input_folder = "Data/Raw Data"
output_folder = "Data/Transformed Data"

os.makedirs(output_folder, exist_ok=True)

stock_data = {}

for root, dirs, files in os.walk(input_folder):

    for file in files:

        if file.endswith(".yaml") or file.endswith(".yml"):

            file_path = os.path.join(root, file)
            print("Reading:", file_path)

            with open(file_path, "r") as f:
                data = yaml.safe_load(f)

            date = file.split("_")[0]

            for record in data:

                symbol = record.get("Ticker")
                
                row = {
                    "date": date,
                    "open": record.get("open"),
                    "high": record.get("high"),
                    "low": record.get("low"),
                    "close": record.get("close"),
                    "volume": record.get("volume")
                }

                if symbol not in stock_data:
                    stock_data[symbol] = []

                stock_data[symbol].append(row)


for symbol, rows in stock_data.items():

    df = pd.DataFrame(rows)

    csv_path = os.path.join(output_folder, f"{symbol}.csv")

    df.to_csv(csv_path, index=False)


print("Conversion completed!")