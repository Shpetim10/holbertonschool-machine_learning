# Pandas

Introductory `pandas` exercises in Python 3. Most tasks work on historical
Bitcoin price data sampled every minute, covering how to create, load,
inspect, reshape, clean, combine, analyse and plot a `pd.DataFrame`.

## Quick start

```bash
pip install pandas numpy matplotlib
cd pipeline/pandas
./2-main.py            # every N-main.py runs the matching task
```

Each exercise is a pair: `N-name.py` holds the solution and `N-main.py` is a
small script that imports it (with `__import__`, because the file names start
with a digit) and prints the result. `14-visualize.py` is a stand-alone script
and has no main file: run it directly with `./14-visualize.py`.

## Data

The scripts expect the following CSV files in this directory. They are large
and ignored by Git (`*.csv` in `.gitignore`), so you must place them here
yourself:

- `coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv`
- `bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv`

Both have the same columns, one row per minute:

| Column | Meaning |
| --- | --- |
| `Timestamp` | Unix time in seconds |
| `Open`, `High`, `Low`, `Close` | Price at the start, top, bottom and end of the minute |
| `Volume_(BTC)` | Bitcoin traded in that minute |
| `Volume_(Currency)` | USD traded in that minute |
| `Weighted_Price` | Volume-weighted average price |

Minutes without any trade are stored as `NaN` (missing).

## The big picture

The tasks follow the usual order of working on a dataset:

```
 CREATE        LOAD         RESHAPE                 CLEAN         COMBINE        ANALYZE & PLOT
 ──────        ────         ───────                 ─────         ───────        ──────────────
 0 from_numpy  2 from_file  3 rename                8 prune       11 concat      13 analyze
 1 from_dict                4 array                 9 fill        12 hierarchy   14 visualize
                            5 slice
                            6 flip_switch
                            7 high
                            10 index
```

## Files

### Create and load (tasks 0–2)

| File | Description |
| --- | --- |
| `0-from_numpy.py` | `from_numpy(array)` creates a DataFrame from a `np.ndarray`, labeling columns `A`, `B`, `C`, … |
| `1-from_dictionary.py` | Builds a DataFrame `df` from a dictionary, with columns `First` and `Second` and rows `A`–`D`. |
| `2-from_file.py` | `from_file(filename, delimiter)` loads a file into a DataFrame (`pd.read_csv`). |

### Select and reshape (tasks 3–7, 10)

| File | Description |
| --- | --- |
| `3-rename.py` | `rename(df)` renames `Timestamp` to `Datetime`, converts it to datetime values and keeps only `Datetime` and `Close`. |
| `4-array.py` | `array(df)` returns the last 10 rows of `High` and `Close` as a `numpy.ndarray`. |
| `5-slice.py` | `slice(df)` keeps `High`, `Low`, `Close` and `Volume_(BTC)` and selects every 60th row (one per hour). |
| `6-flip_switch.py` | `flip_switch(df)` sorts in reverse chronological order and transposes the result. |
| `7-high.py` | `high(df)` sorts by `High` price in descending order. |
| `10-index.py` | `index(df)` sets `Timestamp` as the DataFrame index. |

### Clean (tasks 8–9)

| File | Description |
| --- | --- |
| `8-prune.py` | `prune(df)` removes rows where `Close` is `NaN`. |
| `9-fill.py` | `fill(df)` drops `Weighted_Price`, forward-fills `Close`, fills missing `High`/`Low`/`Open` with that row's `Close`, and sets missing volumes to 0. |

### Combine (tasks 11–12)

| File | Description |
| --- | --- |
| `11-concat.py` | `concat(df1, df2)` indexes both frames on `Timestamp`, takes the Bitstamp rows up to timestamp `1417411920`, and puts them on top of the Coinbase data with keys `bitstamp` and `coinbase`. |
| `12-hierarchy.py` | `hierarchy(df1, df2)` selects timestamps `1417411980`–`1417417980` from both exchanges, concatenates them, moves `Timestamp` to the first index level and sorts chronologically. |

### Analyze and visualize (tasks 13–14)

| File | Description |
| --- | --- |
| `13-analyze.py` | `analyze(df)` returns descriptive statistics (count, mean, std, min, quartiles, max) for every column except `Timestamp`. |
| `14-visualize.py` | Script that cleans the Coinbase data, keeps 2017 onwards, resamples it to **daily** values and plots it with `matplotlib`. |

## How the cleaning works (tasks 8, 9 and 14)

```
 Raw minute data                         After cleaning
 ───────────────                         ──────────────
 Close  High   Open   Volume             Close  High   Open   Volume
 100    101    99     2.5                100    101    99     2.5
 NaN    NaN    NaN    NaN      ──►       100    100    100    0      (fill, task 9)
 105    106    104    1.0                105    106    104    1.0
```

- `Close` is forward-filled (`ffill`): a minute with no trade keeps the last
  known price.
- `High`, `Low` and `Open` copy that row's `Close`.
- Volumes become `0`, because nothing was traded.
- `prune` (task 8) is the alternative: it simply deletes rows where `Close` is
  missing.

## The hierarchical index (tasks 11–12)

```
 task 11 concat                          task 12 hierarchy
 key first, then Timestamp               Timestamp first, then key

 bitstamp  1417411920  ...               1417411980  bitstamp  ...
           ...                                       coinbase  ...
 coinbase  1417411980  ...               1417412040  bitstamp  ...
           ...                                       coinbase  ...
                        swaplevel + sort_index
```

Putting `Timestamp` first lets you read both exchanges side by side for the
same minute.

## Daily resampling (task 14)

```
 minute rows ──► group by day ──► one row per day

 High          -> max   of the day
 Low           -> min   of the day
 Open, Close   -> mean  of the day
 Volume_(BTC), Volume_(Currency) -> sum of the day
```

The result is printed and drawn as a line chart with `df.plot()`.

## Requirements

- Python 3 with `pandas`, `numpy` and `matplotlib`
- Code follows `pycodestyle` (79 characters per line max)
- Every module and function has a docstring
