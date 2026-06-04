import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print(data.keys())

nav_data = data['data']

df = pd.DataFrame(nav_data)

print(df.head())

import os
os.makedirs("../data/raw", exist_ok=True)  
df.to_csv("../data/raw/hdfc_top100_nav.csv", index=False)

df.to_csv("../data/raw/hdfc_top100_nav.csv", index=False)



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

    df.to_csv(f"../data/raw/{name}_nav.csv", index=False)

    print(f"{name} data saved successfully")
