"""
Script Name: etl_pipeline.py
"""

import pandas as pd

fund_df = pd.read_csv(
    "../data/processed/clean_fund_master.csv"
)

nav_df = pd.read_csv(
    "../data/processed/clean_nav_history.csv"
)

txn_df = pd.read_csv(
    "../data/processed/clean_investor_transactions.csv"
)

fund_df.columns = fund_df.columns.str.strip()
nav_df.columns = nav_df.columns.str.strip()
txn_df.columns = txn_df.columns.str.strip()

nav_df['date'] = pd.to_datetime(
    nav_df['date']
)

nav_df = nav_df.sort_values(
    ['amfi_code', 'date']
)

nav_df['nav'] = nav_df.groupby(
    'amfi_code'
)['nav'].ffill()

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[
    nav_df['nav'] > 0
]

txn_df['transaction_date'] = pd.to_datetime(
    txn_df['transaction_date']
)

txn_df = txn_df[
    txn_df['amount_inr'] > 0
]

txn_df['transaction_type'] = txn_df[
    'transaction_type'
].str.upper()

txn_df['cohort_year'] = txn_df.groupby(
    'investor_id'
)['transaction_date'].transform(
    'min'
).dt.year

nav_df.to_csv(
    "../data/processed/final_nav_history.csv",
    index=False
)

txn_df.to_csv(
    "../data/processed/final_investor_transactions.csv",
    index=False
)

print("\nETL Pipeline Completed Successfully!")