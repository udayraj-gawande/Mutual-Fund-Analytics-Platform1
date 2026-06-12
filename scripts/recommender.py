"""
Script Name: recommender.py
"""

import pandas as pd

fund_df = pd.read_csv(
    "../data/processed/clean_fund_master.csv"
)

sharpe_df = pd.read_csv(
    "../data/processed/sharpe_metrics.csv"
)

fund_df.columns = fund_df.columns.str.strip()
sharpe_df.columns = sharpe_df.columns.str.strip()

df = fund_df.merge(

    sharpe_df[
        ['amfi_code', 'sharpe_ratio']
    ],

    on='amfi_code',

    how='left'
)

risk_appetite = input(
    "Enter risk appetite (Low/Moderate/High): "
)

if risk_appetite == 'Low':

    filtered = df[
        df['risk_category']
        .str.contains(
            'Low',
            case=False,
            na=False
        )
    ]

elif risk_appetite == 'Moderate':

    filtered = df[
        df['risk_category']
        .str.contains(
            'Moderate',
            case=False,
            na=False
        )
    ]

elif risk_appetite == 'High':

    filtered = df[
        df['risk_category']
        .str.contains(
            'High',
            case=False,
            na=False
        )
    ]

else:

    print("Invalid Risk Appetite")

top_funds = filtered.sort_values(

    'sharpe_ratio',

    ascending=False

).head(3)

print("\nTop Recommended Funds\n")

print(

    top_funds[
        [
            'scheme_name',
            'fund_house',
            'risk_category',
            'sharpe_ratio'
        ]
    ]

)