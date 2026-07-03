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

def build_trade_log(result):    
    buy_rows = result[result['signal']]
    exit_rows = result[result['exit_signal']]
    # print(buy_rows)
    # print(exit_rows)    

    trades = []

    for (buy_date,buy_rows),(exit_date,exit_rows)  in zip(buy_rows.iterrows(), exit_rows.iterrows()):
        trade = {
            'entry_date' : buy_date,
            'entry_price': buy_rows['entry_price'],
            'sell_date' : exit_date,
            'sell_price': exit_rows['entry_price'],
            'profit': exit_rows['entry_price'] - buy_rows['entry_price'],
            'percentage': (exit_rows['entry_price'] - buy_rows['entry_price']) / buy_rows['entry_price'] * 100
        }
        trades.append(trade)

    data = pd.DataFrame(trades)
    return data


def calculate_metrics(trade_log):
    total_return = trade_log['percentage'].sum()
    win_rate = (trade_log['percentage'] > 0).mean() * 100
    avg_win = trade_log['percentage'][trade_log['percentage'] > 0].mean()
    avg_loss = trade_log['percentage'][trade_log['percentage'] < 0].mean()
    profit_factor = (trade_log['percentage'][trade_log['percentage'] > 0].sum()) / abs(trade_log['percentage'][trade_log['percentage'] < 0].sum())
    
    return {
        'total_return' : round(total_return,2),
        'win_rate' : round(win_rate,2),
        'avg_win' : avg_win,
        'avg_loss' : avg_loss,
        'profit_factor' : profit_factor
    }


result = get_data('BEL.NS','2025-01-01','2026-07-02','1D')


result = add_sma(data=result,size=13)
result = add_sma(data=result,size=48)
result = generate_signal(data=result,size1=13,size2=48)
trade_log = build_trade_log(result)

output = calculate_metrics(trade_log)
print(output)