import yfinance as yf
import pandas as pd

# Define tickers with their specific date ranges
data_config = {
    "^GSPC": ("1982-06-01", "2026-03-23"),
    "CL=F": ("1982-06-01", "2026-03-23"),
    "HG=F": ("1982-06-01", "2026-03-23"),
}

all_data = {}

for ticker, (start, end) in data_config.items():
    df = yf.download(
        ticker,
        start=start,
        end=end,
        interval="1mo",
        auto_adjust=False,
        progress=False
    )

    if df.empty:
        print(f"No data for {ticker}")
        continue

    # Store and save
    all_data[ticker] = df
    df.to_csv(f"{ticker.replace('=', '').replace('^','')}_monthly.csv")

    print(f"\n{ticker} data:")
    print(df.head())

print("\nDownload complete.")