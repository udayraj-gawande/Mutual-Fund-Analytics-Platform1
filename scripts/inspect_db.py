import sqlite3

def main():
    conn = sqlite3.connect('bluestock_mf.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        t_name = table[0]
        print(f"\nTable: {t_name}")
        cursor.execute(f"PRAGMA table_info({t_name});")
        columns = cursor.fetchall()
        print("Columns:")
        for col in columns:
            print(f"  - {col[1]} ({col[2]})")
        
        cursor.execute(f"SELECT COUNT(*) FROM {t_name};")
        row_count = cursor.fetchone()[0]
        print(f"Row count: {row_count}")
        
        if t_name == 'scheme_performance':
            cols_to_check = ['return_3yr_pct', 'sharpe_ratio', 'alpha', 'expense_ratio_pct', 'max_drawdown_pct']
            for col in cols_to_check:
                cursor.execute(f"SELECT COUNT(*) FROM scheme_performance WHERE {col} IS NULL;")
                null_count = cursor.fetchone()[0]
                print(f"  Null count for {col}: {null_count}")
                
        cursor.execute(f"SELECT * FROM {t_name} LIMIT 3;")
        rows = cursor.fetchall()
        print("First 3 rows:")
        for r in rows:
            print(f"  {r}")
            
    conn.close()

if __name__ == '__main__':
    main()
