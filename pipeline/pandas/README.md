# Pandas

Introductory `pandas` exercises in Python 3. Most tasks work on historical Bitcoin price data sampled every minute, covering how to create, load, inspect, reshape and clean a `pd.DataFrame`.

## Data

The scripts expect the following CSV files in this directory:

- `coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv`
- `bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv`

Both have the columns `Timestamp` (Unix seconds), `Open`, `High`, `Low`, `Close`, `Volume_(BTC)`, `Volume_(Currency)` and `Weighted_Price`, with `NaN` rows for minutes without trades.

## Files

| File | Description |
| --- | --- |
| `0-from_numpy.py` | `from_numpy(array)` creates a DataFrame from a `np.ndarray`, labeling columns `A`, `B`, `C`, … |
| `1-from_dictionary.py` | Builds a DataFrame `df` from a dictionary, with columns `First` and `Second` and rows `A`–`D`. |
| `2-from_file.py` | `from_file(filename, delimiter)` loads a file into a DataFrame. |
| `3-rename.py` | `rename(df)` renames `Timestamp` to `Datetime`, converts it to datetime values and keeps only `Datetime` and `Close`. |
| `4-array.py` | `array(df)` returns the last 10 rows of `High` and `Close` as a `numpy.ndarray`. |
| `5-slice.py` | `slice(df)` keeps `High`, `Low`, `Close` and `Volume_(BTC)` and selects every 60th row. |
| `6-flip_switch.py` | `flip_switch(df)` sorts in reverse chronological order and transposes the result. |
| `7-high.py` | `high(df)` sorts by `High` price in descending order. |
| `8-prune.py` | `prune(df)` removes rows where `Close` is `NaN`. |
| `9-fill.py` | `fill(df)` drops `Weighted_Price`, forward-fills `Close`, fills missing `High`/`Low`/`Open` with that row's `Close`, and sets missing volumes to 0. |
| `10-index.py` | `index(df)` sets `Timestamp` as the DataFrame index. |
| `11-concat.py` | *In progress* – concatenating the Coinbase and Bitstamp DataFrames. |
| `12-hierarchy.py` | *In progress* – building a hierarchical (multi-level) index from both DataFrames. |
| `13-analyze.py` | *In progress* – computing descriptive statistics. |
| `14-visualize.py` | *In progress* – plotting the data with `matplotlib`. |

Each `N-main.py` file is a test script for the matching task, e.g. `./2-main.py`.
