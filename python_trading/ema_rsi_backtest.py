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


data = get_data('INFY.NS', '2025-01-01', '2026-07-15', '1D')
data = add_ema(data,9)
data = add_rsi(data,14)

print(data)