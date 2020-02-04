import matplotlib.pyplot as plt
import pandas as pd
import requests

periods = '3600'
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
    params={
        'periods': periods
    })
data = resp.json()

df = pd.DataFrame(
    data['result'][periods],
    columns=[
        'CloseTime',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'ClosePrice',
        'Volume',
        'NA'
    ]
)

print(df.head())

plt.show(df['ClosePrice'].plot(figsize=(14,7)))
