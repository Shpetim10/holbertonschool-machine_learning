# Data Preparation and Visualization

Exercises on preparing and visualizing the
[Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
dataset (`Telco-Customer-Churn.csv`, 7043 customers, 21 columns) with
`pandas`, `numpy`, `scipy`, `matplotlib` and `seaborn`. The goal is to get the data ready to
predict `Churn`, whether a customer left the company.

## Quick start

```bash
pip install pandas numpy scipy matplotlib seaborn
cd data_analysis/data_preparation_visualization
./0-describe_data.py   # task 0 prints a report
./1-main.py            # every N-main.py runs the matching task
```

Each exercise from task 1 on is a pair: `N-name.py` holds the solution and
`N-main.py` is a small script that imports it (with `__import__`, because the
file names start with a digit) and prints or plots the result.

## Cleaning pipeline (tasks 0–5)

```
 raw CSV → convert_columns → clean_total_charges → remove_duplicates → drop_customerID → precleaned CSV
```

`5-main.py` runs the whole pipeline and saves the result to
`precleaned-Telco-Customer-Churn.csv`.

| Task | File | What it does |
| --- | --- | --- |
| 0 | `0-describe_data.py` | Prints the shape, dtypes, first rows, missing values per column and number of duplicated rows. |
| 1 | `1-plot_missingness.py` | `plot_missingness(df)` draws one tick per missing value, one row of the plot per column. |
| 2 | `2-convert_columns.py` | `convert_columns(df)` turns `TotalCharges` into a number (11 blank values become `NaN`) and `SeniorCitizen` from `0`/`1` into `No`/`Yes`. Modifies `df` in place. |
| 3 | `3-clean_total_charges.py` | `clean_total_charges(df, method='drop')` handles the missing `TotalCharges`: `drop` removes the rows, `median` fills with the median, `impute` fills with `MonthlyCharges * tenure`. Returns a copy. |
| 4 | `4-remove_duplicates.py` | `remove_duplicates(df)` keeps only the first of identical rows. |
| 5 | `5-drop_customerID.py` | `drop_customerID(df)` removes the unique identifier, which carries no information about churn. |

Notes:

- `TotalCharges` is read as text because 11 customers have a blank value
  (all with `tenure` 0), so task 0 shows no missing values; the missing values
  only appear after task 2 (`2-main.py` plots them).
- With the default `drop` method the cleaned dataset has 7032 rows.
- An unknown `method` in task 3 leaves the data unchanged.

## Visualization (tasks 6–9)

These tasks read the cleaned dataset produced by `5-main.py`
(`precleaned-Telco-Customer-Churn.csv`), so run that first.

| Task | File | What it does |
| --- | --- | --- |
| 6 | `6-plot_churn_distribution.py` | `plot_churn_distribution(df)` draws a bar chart of the number of customers in each `Churn` class, to show the class balance of the target. |
| 7 | `7-plot_categorical_distributions.py` | `plot_categorical_distributions(df, columns_to_plot=None)` draws a bar chart of value counts for each categorical feature in a grid of 3 columns. Defaults to every text column except `Churn`. Saves the figure to `Task_7.png`. |
| 8 | `8-plot_continuous_distributions.py` | `plot_continuous_distributions(df, columns_to_plot=None)` draws, for each numeric feature, a histogram with a KDE curve and a horizontal boxplot side by side. Defaults to every numeric column. Saves the figure to `Task_8.png`. |
| 9 | `9-plot_correlation_heatmap.py` | `plot_correlation_heatmap(df)` draws an annotated heatmap of the Pearson correlations between the continuous numeric features (columns with two or fewer unique values are ignored). The color scale is fixed to [-1, 1]. |

Notes:

- Tasks 7 and 8 return `None` without drawing anything if there are no
  columns to plot.
- Task 9 needs `seaborn`; the other plots only use `matplotlib` (and `scipy`
  for the KDE in task 8).
- Because task 2 turns `SeniorCitizen` into `No`/`Yes`, it is treated as a
  categorical feature in task 7 and left out of the heatmap in task 9.

## Progress

| Task | File | Status |
| --- | --- | --- |
| 0 | `0-describe_data.py` | Done |
| 1 | `1-plot_missingness.py` | Done |
| 2 | `2-convert_columns.py` | Done |
| 3 | `3-clean_total_charges.py` | Done |
| 4 | `4-remove_duplicates.py` | Done |
| 5 | `5-drop_customerID.py` | Done |
| 6 | `6-plot_churn_distribution.py` | Done |
| 7 | `7-plot_categorical_distributions.py` | Done |
| 8 | `8-plot_continuous_distributions.py` | Done |
| 9 | `9-plot_correlation_heatmap.py` | Done |
| 10–17 | | Not started |
