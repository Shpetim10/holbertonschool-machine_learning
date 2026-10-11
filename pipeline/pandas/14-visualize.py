#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Drop Weighted_Price columns
df = df.drop(columns=["Weighted_Price"])

# Rename Timestamp column to Date
df = df.rename(columns={"Timestamp": "Date"})

# Convert Timestamp dalues to Date
df["Date"] = pd.to_datetime(df["Date"], unit="s")

# Set Date as Index
df = df.set_index("Date")

# Fill nan close values
df['Close'] = df['Close'].ffill()

# Fill na values of High, Low, Open with Close values
for col in ['High', 'Low', 'Open']:
    df[col] = df[col].fillna(df['Close'])

# Fill na values of Volume_(BTC) and Volume_(Currency) with 0
for col in ['Volume_(BTC)', 'Volume_(Currency)']:
    df[col] = df[col].fillna(0)

# Slice data from 2017
df = df.loc["2017":]

# Resampling
df = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Print
print(df)

# Plotting
df.plot()
plt.show()
