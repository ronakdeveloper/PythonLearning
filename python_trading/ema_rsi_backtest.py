from sma_crossover_backtest import get_data

def add_ema(data,size):
    # naming sma based on size of sma
    name = 'ema' + str(size)    

    # adding column and data into dataframe
    data[name] = data['close'].ewm(span=size).mean()   

    return data

def add_rsi(data,size):
    data['delta'] = data['close'].diff()
    
    data['gain'] = data['delta'].where(data['delta'] > 0,0)
    data['loss'] = -data['delta'].where(data['delta'] < 0,0) 

    data['avg_gain'] = data['gain'].ewm(span=size).mean()
    data['avg_loss'] = data['loss'].ewm(span=size).mean()

    data['rs'] = data['avg_gain'] / data['avg_loss']
    data['rsi'] = 100 - (100 / (1 +  data['rs']))
    data['rsi'] = (data['rsi'].fillna(0))
    
    data.drop(columns=['delta','gain','loss','avg_gain','avg_loss','rs'],inplace=True)
    return data

def generate_signal(data, fast_ema, rsi_level, slow_ema):
    fastema = 'ema' + str(fast_ema)
    slowema = 'ema' + str(slow_ema)
    # Phase 1 — pre-calculate helper columns before loop
    data['rsi_prev']  = data['rsi'].shift(1)
    data['rsi_min5']  = data['rsi'].rolling(5).min()
    data['signal']      = False
    data['exit_signal'] = False

    # Phase 2 — state tracking loop
    in_signal = False
    day_held = 0

    for date, row in data.iterrows():

        if not in_signal:
            buy = (
                row['close']    > row[fastema]   and
                row['rsi']      > rsi_level  and
                row['rsi_prev'] < rsi_level  and
                row['rsi_min5'] < 40 and
                row['close'] >  row[slowema]
            )
            if buy:
                data.loc[date, 'signal'] = True
                in_signal = True
                day_held = 0
                print(f"BUY fired: {date}, in_signal={in_signal}")
        

        elif day_held >= 5 and in_signal:
            exit = (
                row['close'] < row[slowema] or
                (row['rsi'] < rsi_level and row['rsi_prev'] > rsi_level)
            )
            if exit:
                data.loc[date, 'exit_signal'] = True
                in_signal = False
        
        day_held += 1

    print("Total BUY signals:", data['signal'].sum())
    print("Total EXIT signals:", data['exit_signal'].sum())
    print(data[data['signal']][['signal', 'exit_signal']])
    # entry price is next day open
    data['entry_price'] = data['open'].shift(-1)
    
    # clean up helper columns
    data.drop(columns=['rsi_prev', 'rsi_min5'], inplace=True)
    
    return data

data = get_data('INFY.NS', '2025-01-01', '2026-07-15', '1D')
data = add_ema(data,9)
data = add_rsi(data,14)
data = add_ema(data,21)
data = generate_signal(data, fast_ema=9, rsi_level=50, slow_ema=21)

print(data[data['signal']])
print(data[data['exit_signal']])