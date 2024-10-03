import pandas as pd
import datetime as dt

full_date_range = pd.date_range(start=dt.datetime(2024, 1, 1), end=dt.datetime(2024, 10, 2), freq='D')

transactions = pd.read_csv("Super/UniSuper/Transactions.csv")
transactions["Date"] = pd.to_datetime(transactions["Date"], format="%d/%m/%Y")

transactions_sorted = transactions.sort_values(by='Date')
transactions_sorted['Balance'] = transactions_sorted['Amount'].cumsum()

closing_balance_of_day = transactions_sorted.drop_duplicates(subset=['Date'], keep='first')

closing_balance_of_day.set_index('Date', inplace=True)

super_reindexed = closing_balance_of_day.reindex(full_date_range)

super_ffilled = super_reindexed.ffill()
super_filled = super_ffilled.bfill()

super_processed = pd.DataFrame()
super_processed["Date"] = super_filled.index
super_processed.set_index("Date", inplace=True)
super_processed["Super"] = super_filled["Balance"]

super_processed.to_csv("TEMP/super.csv")

super_processed.to_csv("TEMP/super.csv")