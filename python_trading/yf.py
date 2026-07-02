import yfinance as yf

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

    return data


result = getdata('ADANIPOWER.NS','2026-01-01','2026-07-02','1D')

result = add_sma(data=result,size=5)
result = add_sma(data=result,size=20)
result = generate_signal(data=result,size1=5,size2=20)
print(result[result['signal']])
print(result[result['exit_signal']])

# df['sma_5'] = df['close'].rolling(window=5).mean()    
# df['sma_20'] = df['close'].rolling(window=20).mean()

# print(df[df['signal']])
# print(df[df['exit_signal']])
# print(df[df['signal'] == True])

