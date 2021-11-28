import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
import csv
import strip

from secrets import IEX_CLOUD_API_TOKEN



with open('C:/Users/Yassi/PycharmProjects/StocksTrading/algorithmic-trading-python/starter_files/sp_500_stocks.csv',
          newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        symbol = str(row).strip("['']")
        api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
        data = requests.get(api_url).json()

        price = data['latestPrice']
        market_cap = data['marketCap']
        my_columns = ['Ticker', 'Stocks Price', 'Market Capitalisation', 'Number of Shares to Buy']
        final_dataframe = pd.DataFrame(columns=my_columns)
        a = final_dataframe.append(
            pd.Series(
                [
                    symbol,
                    price,
                    market_cap,
                    'N/A'
                ],
                index=my_columns
            ),
            ignore_index=True
        )
        print(a)
