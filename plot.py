import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Directory containing the CSV files
cwd = os.getcwd()
directory = os.path.join(cwd, "TEMP")

# Get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(directory, '*.csv'))

# Initialize an empty DataFrame
combined_df = pd.DataFrame()

# Read each CSV file and merge them into the combined DataFrame
for file in csv_files:
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    combined_df = combined_df.add(df, fill_value=0)

# Reset the index if needed
combined_df.reset_index(inplace=True)
combined_df.set_index("Date", inplace=True)

combined_df = combined_df[["Transactions", "Savings", "Super"]]


# Plotting
ax = combined_df.plot(kind='area', stacked=True, alpha=0.5, linestyle='None')  # Set alpha to 0.5 for transparency
#ax.plot(net_worth_processed["Savings"] + net_worth_processed["Transactions"])
ax.minorticks_off()
ax.xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator())
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b'))
ax.set_ylabel("AUD")
ax.set_title("Tom's Net Worth")

plt.legend()  # Show legend for the added lines
plt.show()
