# Data Documentation: Fixed Income & Macro Econometrics

## Directory Structure
- `raw/`: Sovereign yield curve observations, Treasury term structures, and Federal Reserve Economic Data (FRED).
- `processed/`: Nelson-Siegel fitted yield curves, cointegrating residuals, and outlier diagnostic matrices.

## Data Sources & Acquisition
- **Federal Reserve Economic Data (FRED)**: Real Personal Consumption Expenditures (PCEC96) and Real Disposable Personal Income (DPIC96). Can be acquired via `pandas_datareader` or `fredapi`.
- **Sovereign Yield Data**: Benchmark government bond yields across short-term bills to 30-year sovereign bonds.
- **Synthetic/Empirical Econometrics**:
  - Controlled collinear predictors generated via bivariate normal processes with specified correlation $ho$.
  - Cook's Distance and regression leverage diagnostics evaluated on macro-financial series.
