"""
Script Name: compute_metrics.py
"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    "../data/processed/final_nav_history.csv"
)

df.columns = df.columns.str.strip()

df['date'] = pd.to_datetime(
    df['date']
)

df = df.sort_values(
    ['amfi_code', 'date']
)

df['daily_return'] = df.groupby(
    'amfi_code'
)['nav'].pct_change()

cagr_df = df.groupby(
    'amfi_code'
).agg(

    start_nav=('nav', 'first'),

    end_nav=('nav', 'last'),

    n_days=('date', 'count')

).reset_index()

cagr_df['years'] = (
    cagr_df['n_days'] / 252
)

cagr_df['CAGR'] = (

    cagr_df['end_nav']
    /
    cagr_df['start_nav']

) ** (

    1 / cagr_df['years']

) - 1

rf = 0.065

sharpe_df = df.groupby(
    'amfi_code'
)['daily_return'].agg(

    mean_return='mean',

    std_return='std'

).reset_index()

sharpe_df['sharpe_ratio'] = (

    (
        sharpe_df['mean_return']
        -
        rf/252
    )

    /

    sharpe_df['std_return']

) * np.sqrt(252)

negative_returns = df[
    df['daily_return'] < 0
]

downside_std = negative_returns.groupby(
    'amfi_code'
)['daily_return'].std().reset_index()

downside_std.rename(

    columns={
        'daily_return': 'downside_std'
    },

    inplace=True
)

sortino_df = sharpe_df.merge(
    downside_std,
    on='amfi_code'
)

sortino_df['sortino_ratio'] = (

    (
        sortino_df['mean_return']
        -
        rf/252
    )

    /

    sortino_df['downside_std']

) * np.sqrt(252)

df['running_max'] = df.groupby(
    'amfi_code'
)['nav'].cummax()

df['drawdown'] = (

    df['nav']
    /
    df['running_max']

) - 1

max_dd = df.groupby(
    'amfi_code'
)['drawdown'].min().reset_index()

max_dd.rename(

    columns={
        'drawdown': 'max_drawdown'
    },

    inplace=True
)

var_df = df.groupby(
    'amfi_code'
)['daily_return'].quantile(
    0.05
).reset_index()

var_df.rename(

    columns={
        'daily_return': 'VaR_95'
    },

    inplace=True
)

sharpe_df.to_csv(
    "../data/processed/sharpe_metrics.csv",
    index=False
)

sortino_df.to_csv(
    "../data/processed/sortino_metrics.csv",
    index=False
)

max_dd.to_csv(
    "../data/processed/max_drawdown.csv",
    index=False
)

var_df.to_csv(
    "../data/processed/var_metrics.csv",
    index=False
)

print("\nFinancial Metrics Computed Successfully!")