import yfinance as yf

df = yf.download(
   tickers= "ADANIPOWER.NS",
    start='2026-01-01',
    end='2026-06-30',
    interval='1D',
    multi_level_index=False
)

## lowercase everything after download
df.columns = df.columns.str.lower()

print(df.head())
df.info()