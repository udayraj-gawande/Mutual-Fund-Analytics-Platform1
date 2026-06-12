# 📊 Mutual Fund Analytics Platform

A comprehensive end-to-end analytics platform for Indian mutual funds built with Python, SQLite, and Power BI.  
It covers data ingestion, ETL cleaning, quantitative risk/return metrics, a fund recommender engine, and an interactive dashboard.

---

## 🗂️ Project Structure

```
Mutual-Fund-Analytics-Platform/
│
├── run_pipeline.py              ← Master pipeline runner (start here)
│
├── scripts/                     ← Python automation scripts
│   ├── live_nav_fetch.py        │  Fetch live NAV data from MF API
│   ├── etl_pipeline.py          │  Clean & normalise all raw CSVs
│   ├── compute_metrics.py       │  Sharpe, CAGR, VaR, CVaR, drawdown
│   ├── load_to_db.py            │  Load processed data into SQLite
│   ├── recommender.py           │  Rule-based fund recommender
│   ├── inspect_notebooks.py     │  Audit notebook code cells
│   
│
├── data/
│   ├── raw/                     ← Source CSV files (AMFI / MF API)
│   ├── processed/               ← Cleaned CSVs & derived metrics
│   
│
├── notebook/                    ← Jupyter notebooks (01 → 05)
│  
│
├── sql/                         ← SQLite schema & analytical queries
│   └
│
├── dashboard/                   ← Power BI .pbix and PDF export
│  
│
├── reports/                     ← Final report PDF & presentation PPTX
│  
│
└── bluestock_mf.db              ← SQLite database (auto-generated)
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/udayraj-gawande/Mutual-Fund-Analytics-Platform.git
cd Mutual-Fund-Analytics-Platform
```

### 2. Set Up a Virtual Environment

```bash
python -m venv env

env\Scripts\activate


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Full Pipeline

```bash
python run_pipeline.py
```

This executes all four pipeline steps in order:

| Step | Script | What it does |
|------|--------|--------------|
| 1 | `live_nav_fetch.py` | Pulls latest NAV data from the MF API |
| 2 | `etl_pipeline.py` | Cleans all raw CSVs → `data/processed/` |
| 3 | `compute_metrics.py` | Computes Sharpe, CAGR, VaR, CVaR per scheme |
| 4 | `load_to_db.py` | Loads processed data into `bluestock_mf.db` |

---

## ⚙️ Pipeline Options

```bash
# Skip live API fetch (use existing raw data — offline mode)
python run_pipeline.py --skip-fetch

# Stop immediately on the first error
python run_pipeline.py --fail-fast

# Run only specific steps
python run_pipeline.py --steps etl metrics db

# See all options
python run_pipeline.py --help
```

---

## 📈 Fund Recommender

```bash
# Default: moderate risk profile, top 5 funds
python scripts/recommender.py

# Aggressive investor, top 10 funds
python scripts/recommender.py --profile aggressive --top 10

# Conservative investor
python scripts/recommender.py --profile conservative
```

---

## 📓 Notebooks

Five Jupyter notebooks walk through the full analysis:

| Notebook | Topic |
|----------|-------|
| `01_data_ingestion.ipynb` | Data sourcing & setup |
| `02_data_cleaning.ipynb` | Cleaning & validation |
| `03_eda_analysis.ipynb` | Exploratory analysis |
| `04_performance_analytics.ipynb` | Returns, Sharpe, drawdown |
| `05_advanced_analytics.ipynb` | VaR/CVaR, SIP cohorts, HHI |

```bash
jupyter notebook
```

---

## 🗄️ Database

The SQLite database `bluestock_mf.db` is populated automatically by the pipeline.  
Analytical queries are in [`sql/queries.sql`](sql/queries.sql).

```bash
# Run all queries
sqlite3 bluestock_mf.db < sql/queries.sql
```

---

## 📊 Dashboard

Open [`dashboard/bluedstock_mf.pbix`](dashboard/bluedstock_mf.pbix) in Power BI Desktop.  
A static export is available as [`dashboard/bluedstock_mf.pdf`](dashboard/bluedstock_mf.pdf).

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation |
| `numpy` | Numerical computations |
| `requests` | HTTP calls to MF API |
| `sqlalchemy` | SQLite ORM / connection |
| `colorama` | Coloured terminal output (optional) |

Install all at once:
```bash
pip install pandas numpy requests sqlalchemy colorama
```

---

## 📁 Key Metrics Computed

| Metric | Description |
|--------|-------------|
| **CAGR** | Compound Annual Growth Rate over full NAV history |
| **Sharpe Ratio** | Risk-adjusted return (vs 6.5% risk-free rate) |
| **Volatility** | Annualised standard deviation of daily returns |
| **Max Drawdown** | Largest peak-to-trough NAV decline |
| **VaR (5%)** | Value-at-Risk at 95% confidence |
| **CVaR (5%)** | Expected Shortfall beyond VaR threshold |

---

## 📄 Reports

- 📄 [Final Report (PDF)](reports/Mutual_Fund_Analytics_Final_Report.pdf)
- 📑 [Presentation (PPTX)](reports/Mutual_Fund_Analytics_Presentation%20(1).pptx)

---

## 🤝 Author

**Uday Raj Gawande**  
[GitHub](https://github.com/udayraj-gawande) · [LinkedIn](https://linkedin.com/in/udayraj-gawande)

---

*Built as part of the Bluestock Fintech Internship — June 2026*
