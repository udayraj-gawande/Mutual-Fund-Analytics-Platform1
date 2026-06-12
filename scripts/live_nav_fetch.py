"""
Script Name: live_nav_fetch.py
"""

import pandas as pd
import requests

schemes = {

    "sbi_bluechip": 119551,

    "icici_bluechip": 120503,

    "nippon_large_cap": 118632,

    "axis_bluechip": 119092,

    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_data = data['data']

    df = pd.DataFrame(nav_data)

    df.to_csv(
        f"../data/raw/{name}_nav.csv",
        index=False
    )

    print(f"{name} data saved successfully")

print("\nAll NAV files fetched successfully!")