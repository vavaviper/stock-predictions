# Stock Market Predictions

## Project Summary

This project explores whether macroeconomic and commodity indicators can predict the S&P 500 index using classical machine-learning regression models. We collect 15 years of monthly data (2011–2026) from **Yahoo Finance** and **FRED**, engineer calendar and smoothing features, and train five regression models — Simple Linear Regression, Lasso, Ridge, Random Forest, and SVR — evaluating each with MSE, RMSE, MAE, R², and directional accuracy.

### Features used

| Feature | Source |
|---|---|
| S&P 500 (target) | Yahoo Finance (`^GSPC`) |
| Crude Oil | Yahoo Finance (`CL=F`) |
| US 10-Year Treasury Yield | Yahoo Finance (`^TNX`) |
| Copper | Yahoo Finance (`HG=F`) |
| Steel PPI | FRED (`WPU101707`) |
| CPI (Inflation) | FRED (`CPIAUCSL`) |
| Unemployment Rate | FRED (`UNRATE`) |

### Key findings

- CPI and Year are the most influential features across all models.
- Tree-based models (Random Forest) capture nonlinear patterns but struggle to extrapolate beyond the training regime.
- Linear models (Lasso, Ridge) perform comparably, with Lasso naturally pruning weak features.
- All models produce negative or near-zero R² on the held-out test set, highlighting the inherent difficulty of predicting equity markets with monthly macro data alone.

## Folder Structure

```
stock-predictions/
├── README.md                       # This file
├── requirements.txt                # Pinned Python dependencies
├── data_collection.ipynb           # Downloads & combines all data sources
├── data_exploration.ipynb          # EDA, correlation analysis, visualizations
├── data/
│   ├── combined_monthly.csv              # Full 2011-2026 monthly dataset
│   ├── combined_monthly_no_2020.csv      # Dataset with 2020 rows removed
│   ├── combined_monthly_running_avg.csv  # 2020 values replaced by running averages
│   └── combined_monthly_running_avg_20.csv
├── models/
│   ├── regression.ipynb                  # Simple Linear Regression
│   ├── lasso_regression.ipynb            # Lasso Regression (L1)
│   ├── ridge_regression.ipynb            # Ridge Regression (L2)
│   ├── random_forest_regression.ipynb    # Random Forest Regressor
│   └── svr_regression.ipynb              # Support Vector Regression
└── .venv/                          # Virtual environment (not tracked)
```

## Dependencies

All dependencies are pinned in `requirements.txt`:

| Package | Version |
|---|---|
| numpy | 2.4.3 |
| pandas | 2.2.3 |
| matplotlib | 3.10.8 |
| scikit-learn | 1.7.2 |
| yfinance | 1.2.0 |

**Prerequisites:** Python >= 3.12, git

## How to Run

### 1. Clone and set up the environment

```bash
git clone https://github.com/vavaviper/stock-predictions.git
cd stock-predictions

python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

pip install -r requirements.txt
pip install notebook ipykernel
python -m ipykernel install --user --name stock-predictions --display-name "Python (stock-predictions)"
```

### 2. Launch Jupyter

```bash
jupyter notebook
```

### 3. Run notebooks in order

| Step | Notebook | Purpose |
|---|---|---|
| 1 | `data_collection.ipynb` | Downloads data from Yahoo Finance & FRED, produces CSVs in `data/` |
| 2 | `data_exploration.ipynb` | EDA: distributions, correlations, time-series plots |
| 3 | `models/regression.ipynb` | Simple Linear Regression baseline |
| 4 | `models/lasso_regression.ipynb` | Lasso with GridSearchCV + TimeSeriesSplit |
| 5 | `models/ridge_regression.ipynb` | Ridge with GridSearchCV + TimeSeriesSplit |
| 6 | `models/random_forest_regression.ipynb` | Random Forest with GridSearchCV + TimeSeriesSplit |
| 7 | `models/svr_regression.ipynb` | SVR with GridSearchCV + TimeSeriesSplit |

## Reproducibility Instructions

1. **Use the exact dependency versions** listed in `requirements.txt` (`pip install -r requirements.txt`).
2. **Run `data_collection.ipynb` first** — it fetches live data from Yahoo Finance and FRED, so results may shift slightly as new months are published. The CSVs committed in `data/` capture the snapshot used for the results in the model notebooks.
3. **All model notebooks use a fixed `random_state=42`** and deterministic time-aware train/test splits (first 80% train, last 20% test) to ensure consistent results across runs.
4. **Hyperparameter tuning uses `TimeSeriesSplit(n_splits=5)`** to prevent temporal leakage during cross-validation.
5. **To reproduce the exact results shown in the committed notebooks**, use the CSV files already in `data/` rather than re-running `data_collection.ipynb`, which pulls the latest data.

## Notes

- `data_collection.ipynb` requires an internet connection to download data.
- The `combined_monthly_no_2020.csv` variant removes COVID-era rows entirely; `combined_monthly_running_avg.csv` smooths them with a cumulative running average to reduce volatility spikes.
- Model notebooks read from `../data/` using relative paths — always launch Jupyter from the repository root.
