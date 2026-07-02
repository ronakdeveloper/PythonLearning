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


result = get_data('ADANIPOWER.NS','2026-01-01','2026-07-02','1D')

result = add_sma(data=result,size=5)
result = add_sma(data=result,size=20)
result = generate_signal(data=result,size1=5,size2=20)


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
        'profit': exit_rows['entry_price'] - buy_rows['entry_price']
    }
    trades.append(trade)

df = pd.DataFrame(trades)
print(df)