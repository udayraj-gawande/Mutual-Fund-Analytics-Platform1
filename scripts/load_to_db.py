"""
Script Name: load_to_db.py
"""

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'sqlite:///../data/db/bluestock_mf.db'
)

fund_df = pd.read_csv(
    "../data/processed/clean_fund_master.csv"
)

nav_df = pd.read_csv(
    "../data/processed/final_nav_history.csv"
)

txn_df = pd.read_csv(
    "../data/processed/final_investor_transactions.csv"
)

fund_df.to_sql(
    'dim_fund',
    engine,
    if_exists='replace',
    index=False
)

nav_df.to_sql(
    'fact_nav',
    engine,
    if_exists='replace',
    index=False
)

txn_df.to_sql(
    'fact_transactions',
    engine,
    if_exists='replace',
    index=False
)

print("\nAll tables loaded successfully!")