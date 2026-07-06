import yfinance as yf
import pandas as pd

def get_data(name,fromdate,todate,timeframe):    
    df = yf.download(
    tickers= name,
        start=fromdate,
        end=todate,
        interval=timeframe,
        multi_level_index=False
    )

    ## lowercase everything after download
    df.columns = df.columns.str.lower()
    
    return df

def add_sma(data,size):
    name = 'sma' + str(size)    

    data[name] = data['close'].rolling(window=size).mean()   

    return data


def generate_signal(data,size1,size2):
    fastsma = 'sma' + str(size1)
    slowsma = 'sma' + str(size2)
    data['signal'] = (
        (data[fastsma] > data[slowsma]) &
        (data[fastsma].shift(1) < data[slowsma].shift(1))
    )

    data['exit_signal'] = (
        (data[fastsma] < data[slowsma]) &
        (data[fastsma].shift(1) > data[slowsma].shift(1))
    )

    data['entry_price'] = data['open'].shift(-1)
    return data

def build_trade_log(result,amount):    
    buy_rows = result[result['signal']]
    exit_rows = result[result['exit_signal']]
    # print(buy_rows)
    # print(exit_rows)    

    trades = []
    capital = amount 

    for (buy_date,buy_rows),(exit_date,exit_rows)  in zip(buy_rows.iterrows(), exit_rows.iterrows()):
        trade = {
            'entry_date' : buy_date,
            'entry_price': buy_rows['entry_price'],
            'sell_date' : exit_date,
            'sell_price': exit_rows['entry_price'],
            'profit': exit_rows['entry_price'] - buy_rows['entry_price'],
            'percentage': (exit_rows['entry_price'] - buy_rows['entry_price']) / buy_rows['entry_price'] * 100
        }
        trade['multiplier'] = 1 + (trade['percentage'] / 100)
        trades.append(trade)

    data = pd.DataFrame(trades)
    data['equity'] = capital * data['multiplier'].cumprod()

    return data


def calculate_metrics(trade_log):
    total_return = trade_log['percentage'].sum()
    win_rate = (trade_log['percentage'] > 0).mean() * 100
    avg_win = trade_log['percentage'][trade_log['percentage'] > 0].mean()
    avg_loss = trade_log['percentage'][trade_log['percentage'] < 0].mean()

    wins = trade_log['percentage'][trade_log['percentage'] > 0].sum()
    losses = trade_log['percentage'][trade_log['percentage'] < 0].sum()

    if losses == 0:
        profit_factor = float('inf')
    else:
        profit_factor = wins / losses
    
    return {
        'total_return' : round(total_return,2),
        'win_rate' : round(win_rate,2),
        'avg_win' : round(avg_win,2),
        'avg_loss' : round(avg_loss,2),
        'profit_factor' : round(profit_factor,2)
    }

def run_backtest(symbols, start, end, fast, slow, timeframe):
    all_results = []

    for symbol in symbols:
        data = get_data(symbol, start, end, timeframe)
        data = add_sma(data,size=slow)
        data = add_sma(data,size=fast)
        data = generate_signal(data,slow,fast)
        data = build_trade_log(data,100000)
        print(data)
        metrics = calculate_metrics(data)

        metrics['symbol'] = symbol

        all_results.append(metrics)
    summary = pd.DataFrame(all_results)
    return summary

# symbols = ['PSPPROJECT.NS','EIEL.NS','CUPID.NS','INFY.NS']
symbols = ['KPITTECH.NS']
summary = run_backtest(
    symbols=symbols, start='2025-01-01', end='2026-07-06', fast=20, slow=50, timeframe='1D'
)

print(summary)