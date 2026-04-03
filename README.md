# stock-predictions

This project uses Jupyter notebooks to collect market/economic data, explore the dataset, and train regression models.

## Install dependencies

1. Clone the repository and move into the project folder.

```powershell
git clone <your-repo-url>
cd stock-predictions
```

2. Create and activate a virtual environment.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the Python packages used by the notebooks.

```powershell
pip install -r requirements.txt
```

4. Install Jupyter support in the same environment.

```powershell
pip install notebook ipykernel
python -m ipykernel install --user --name stock-predictions --display-name "Python (stock-predictions)"
```

## Run the notebooks

Start Jupyter from the repository root so notebook paths like `data/combined_monthly.csv` resolve correctly.

```powershell
jupyter notebook
```

Suggested notebook order:

1. `data_collection.ipynb`
2. `data_exploration.ipynb`
3. notebooks in `models/`

## Notes

- `data_collection.ipynb` downloads data from Yahoo Finance and FRED, so it needs an internet connection when you run it.
- The model and exploration notebooks expect generated CSV files inside the `data/` folder.
