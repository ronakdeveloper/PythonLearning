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


def generate_signal(data,fast,slow):
    fastsma = 'sma' + str(fast)
    slowsma = 'sma' + str(slow)
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

def build_trade_log(result,starting_capital,stop_loss_per,risk_per):    

    trades = []
    in_trade = False
    entry_date = None
    entry_price = None
    exit_date = None
    exit_price = None
    sl_price = None
    exit_reason = None
    starting_capital = starting_capital
    capital = starting_capital 
    risk_amount = capital * risk_per / 100
    risk_per_share = None
    shares = None
    deployed = None

    for date,row in result.iterrows():

        if row['signal'] == True and in_trade == False:
            in_trade = True
            entry_date = date
            entry_price = row['entry_price']
            sl_price =  row['entry_price'] * (1 - stop_loss_per / 100)
            risk_per_share = row['entry_price'] - sl_price
            shares = round(risk_amount / risk_per_share,0)
            deployed = shares * row['entry_price']

            
        elif in_trade:
            
            # check stop loss first
            if row['low'] < sl_price:
                in_trade = False 
                exit_price = sl_price
                exit_date = date
                exit_reason = 'Stop loss'  

            elif row['exit_signal'] == True and in_trade == True: 
                in_trade = False
                exit_date = date
                exit_price = row['entry_price']
                exit_reason = 'Sell Signal'  

            if not in_trade:
                trade = {
                    'entry_date' : entry_date,
                    'entry_price': entry_price,
                    'Qty' : shares,
                    'Investment' : deployed,
                    'sell_date' : exit_date,
                    'sell_price': exit_price,
                    'Status': exit_reason,
                    'profit': shares * (exit_price - entry_price),
                    'percentage': (exit_price - entry_price) / entry_price * 100
                }
                        
                trade['multiplier'] = 1 + (trade['percentage'] / 100)
                trades.append(trade)
                capital = capital + trade['profit']
                risk_amount = capital * risk_per / 100

    data = pd.DataFrame(trades)
    data['equity'] = round(starting_capital + data['profit'].cumsum(),2)

    return data

def calculate_metrics(trade_log,starting_capital):
    final_equity = trade_log['equity'].iloc[-1]

    total_return = (final_equity - starting_capital) / starting_capital * 100
    win_rate = (trade_log['percentage'] > 0).mean() * 100
    avg_win = trade_log['percentage'][trade_log['percentage'] > 0].mean()
    avg_loss = trade_log['percentage'][trade_log['percentage'] < 0].mean()

    wins = trade_log['percentage'][trade_log['percentage'] > 0].sum()
    losses = trade_log['percentage'][trade_log['percentage'] < 0].sum()

    peak = trade_log['equity'].cummax()
    drawdown = (trade_log['equity'] - peak) / peak * 100
    max_drawdown = drawdown.min()

    if losses == 0:
        profit_factor = float('inf')
    else:
        profit_factor = abs(wins / losses)

    avg_win  = avg_win  if not pd.isna(avg_win)  else 0.0
    avg_loss = avg_loss if not pd.isna(avg_loss) else 0.0
    
    return {
        'total_return' : round(total_return,2),
        'win_rate' : round(win_rate,2),
        'avg_win' : round(avg_win,2),
        'avg_loss' : round(avg_loss,2),
        'profit_factor' : round(profit_factor,2),
        'max_drawdown' : round(max_drawdown,2)
    }

def run_backtest(symbols, start, end, fast, slow, timeframe, starting_capital, stop, risk):
    all_results = []

    for symbol in symbols:
        data = get_data(symbol, start, end, timeframe)
        data = add_sma(data,size=slow)
        data = add_sma(data,size=fast)
        data = generate_signal(data,fast,slow)
        data = build_trade_log(data,starting_capital,stop,risk)
        print(data)
        metrics = calculate_metrics(data,starting_capital)

        metrics['symbol'] = symbol

        all_results.append(metrics)
    summary = pd.DataFrame(all_results)
    return summary

symbols = ['KPITTECH.NS']
summary = run_backtest(
    symbols=symbols, start='2025-01-01', end='2026-07-06', fast=20, slow=50, timeframe='1D',starting_capital=100000,stop=5,risk=2
)

print(summary)