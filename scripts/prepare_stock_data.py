"""
Download and save a simple monthly Alphabet stock-price dataset for 2025.
The output has two columns: X is a month index starting at 0, and y is the
High-Low midpoint of that month's first trading day.
The small CSV can be read without accessing the network.

To reproduce the data, run
```bash
uv run --no-project --with yfinance python scripts/prepare_stock_data.py
```
"""

from pathlib import Path

import yfinance as yf


def load_stock_price(name: str, start: str, end: str) -> None:
    """Save month indexes and first-day high-low midpoint prices as X and y."""
    project_directory: Path = Path(__file__).resolve().parent.parent
    output_path: Path = project_directory / "data" / name

    daily_prices = yf.Ticker("GOOGL").history(
        start=start,
        end=end,
        interval="1d",
        auto_adjust=False,
    )
    if daily_prices.empty:
        raise RuntimeError("No prices were returned. Check the ticker or data source.")

    daily_prices.index = daily_prices.index.tz_localize(None)
    first_trading_days = daily_prices.groupby(daily_prices.index.to_period("M")).head(1)
    monthly_data = first_trading_days[["High", "Low"]].copy()
    month_index = list(range(len(first_trading_days)))
    monthly_data.insert(0, "X", month_index)
    monthly_data["y"] = (monthly_data["High"] + monthly_data["Low"]) / 2
    monthly_data = monthly_data[["X", "y"]]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    monthly_data.to_csv(output_path, index=False)
    print(f"Saved Stock Price {len(monthly_data)} monthly rows to {output_path}")


if __name__ == "__main__":
    load_stock_price("google_stock_2025.csv", "2025-04-01", "2026-01-01")
    load_stock_price("google_stock_2026.csv", "2026-01-02", "2026-04-01")
