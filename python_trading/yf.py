import yfinance as yf

def run_vwap():
    df = yf.download(
    tickers= "ADANIPOWER.NS",
        start='2025-01-01',
        end='2026-06-30',
        interval='1D',
        multi_level_index=False
    )

    ## lowercase everything after download
    df.columns = df.columns.str.lower()

    df['sma_5'] = df['close'].rolling(window=5).mean()
    df['sma_20'] = df['close'].rolling(window=20).mean()

    df['signal'] = (
        (df['sma_5'] > df['sma_20']) &
        (df['sma_5'].shift(1) < df['sma_20'].shift(1))
    )

    df['exit_signal'] = (
        (df['sma_5'] < df['sma_20']) &
        (df['sma_5'].shift(1) > df['sma_20'].shift(1))
    )

    print(df[df['signal']])
    print(df[df['exit_signal']])
    # print(df[df['signal'] == True])
