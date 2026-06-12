"""
scripts package
---------------
Python scripts for the Mutual Fund Analytics Platform pipeline.

Modules:
    live_nav_fetch   – Fetch live NAV data from the MF API
    etl_pipeline     – Extract → Transform → Load raw CSV data
    compute_metrics  – Risk and return metric computation
    load_to_db       – Load processed data into SQLite
    recommender      – Rule-based fund recommendation engine
    inspect_notebooks – Utility to print Jupyter notebook code cells
"""
