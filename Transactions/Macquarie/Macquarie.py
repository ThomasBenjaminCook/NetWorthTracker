import pandas as pd
import datetime as dt
import os

cwd = os.getcwd()

files = os.listdir(os.path.join(os.path.join(cwd,"Transactions"),"Macquarie"))
csv_files = [file for file in files if file.endswith('.csv')]

for csv in csv_files:

    full_date_range = pd.date_range(start=dt.datetime(2024, 1, 1), end=dt.datetime(2024, 10, 2), freq='D')

    savings = pd.read_csv("Transactions/Macquarie/"+csv)
    savings["Transaction Date"] = pd.to_datetime(savings["Transaction Date"], format="%d %b %Y")

    savings_sorted = savings.sort_values(by='Transaction Date')

    closing_balance_of_day = savings_sorted.drop_duplicates(subset=['Transaction Date'], keep='first')

    closing_balance_of_day.set_index('Transaction Date', inplace=True)

    savings_reindexed = closing_balance_of_day.reindex(full_date_range)

    savings_ffilled = savings_reindexed.ffill()
    savings_filled = savings_ffilled.bfill()

    savings_processed = pd.DataFrame()
    savings_processed["Date"] = savings_filled.index
    savings_processed.set_index("Date", inplace=True)
    savings_processed["Transactions"] = savings_filled["Balance"]

    savings_processed.to_csv("TEMP/"+csv)