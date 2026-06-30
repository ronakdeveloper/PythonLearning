import pandas as pd

data = {
    'date' : ['2026-01-01','2026-01-02','2026-01-03'],  
    'open' : [100,104,105],
    'high' : [106,130,108],
    'low'  : [98,101,60],
    'close': [104,105,98],
    'volume': [150000,320000,210000]
}

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# print(df.info())
print(df.loc['2026-01-01':'2026-01-02'])