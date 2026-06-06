import pandas as pd
from sqlalchemy import create_engine
import os

def load_data():
    
    base_dir = r'c:\Users\Radiusr\Desktop\Mutual-Fund-Analytics-Platform'
    data_dir = os.path.join(base_dir, 'data', 'processed')
    db_path = os.path.join(base_dir, 'bluestock_mf.db')
    
    
    engine = create_engine(f'sqlite:///{db_path}')
    
    
    file_table_mapping = {
        'clean_nav_history.csv': 'fact_nav',
        'clean_investor_transactions.csv': 'investor_transactions',
        'clean_scheme_performance.csv': 'scheme_performance'
    }
    
    for file_name, table_name in file_table_mapping.items():
        file_path = os.path.join(data_dir, file_name)
        if os.path.exists(file_path):
            print(f"Loading {file_name} into table {table_name}...")
            
            df = pd.read_csv(file_path)
            
            
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Successfully loaded {len(df)} rows into {table_name}.")
        else:
            print(f"Warning: File {file_path} not found.")

if __name__ == "__main__":
    load_data()
    print("Database sync complete.")
