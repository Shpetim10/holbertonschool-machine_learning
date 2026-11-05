#!/usr/bin/env python3
"""Describe the raw Telco Customer Churn dataset.

Loads Telco-Customer-Churn.csv and prints a first overview of the data:
its shape, column data types, first rows, number of missing values per
column and number of duplicated rows.
"""
import pandas as pd

# Load the raw dataset
df = pd.read_csv('Telco-Customer-Churn.csv')

# (number of rows, number of columns)
shape = df.shape
# Data type of every column
data_types = df.dtypes
# First 5 rows
head = df.head()
# Number of NaN values per column. Note that blank strings (such as the
# empty TotalCharges values) are not NaN until the column is converted.
missing_count = df.isna().sum()
# Number of rows that are exact copies of an earlier row
duplicates = df.duplicated().sum()

print("Shape:", shape)
print("Dtypes:\n", data_types)
print("First rows:\n", head)
print("Missing values:\n", missing_count)
print("Duplicates:", duplicates)
