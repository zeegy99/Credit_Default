import csv
import pandas as pd
from datetime import datetime
import numpy as np
import math


#Data Collection
corporate_bond_spread = pd.read_csv('data/corporate_bond_spread_csv.csv') #Header: {Date, Value} Shape: (7634, 2) 
corporate_bond_spread = corporate_bond_spread.rename(columns={'Date': 'observation_date'})

FRED_yield_spread = pd.read_csv('data/FRED_high_yield_index_spread_csv.csv') #Header: {observation_date, BAMLH0A0HYM2} Shape: (2644, 2) Start Date: 2016-03-30
unemployment = pd.read_csv('data/unemployment_csv.csv') #Header: {observation_date, UNRATE} #Shape: (120, 2) Start date: 2016-03-01

market_rates = pd.read_csv('data/fed_funds_rate_csv.csv') 
market_rates = market_rates.rename(columns={'Effective Date' : 'observation_date'})
market_rates = market_rates[(market_rates['observation_date'].notna())]
'''Index(['Effective Date', 'Rate Type', 'Rate (%)', '1st Percentile (%)',
       '25th Percentile (%)', '75th Percentile (%)', '99th Percentile (%)',
       'Volume ($Billions)', 'Target Rate From (%)', 'Target Rate To (%)',
       'Intra Day - Low (%)', 'Intra Day - High (%)', 'Standard Deviation (%)',
       '30-Day Average SOFR', '90-Day Average SOFR', '180-Day Average SOFR',
       'SOFR Index', 'Revision Indicator (Y/N)', 'Footnote ID'],
      dtype='str')

      Shape: (11051, 19)

      '''

#Data Normalization
data = [corporate_bond_spread, FRED_yield_spread, unemployment, market_rates]
'''Earliest is 2016-03-01, Latest is 2026-02-01'''
if 1:
    for dataset in data:
        min_date = dataset['observation_date'].iloc[0]
        max_date = dataset['observation_date'].iloc[-1]
        print(min_date, max_date)

normal_format_string = "%Y-%m-%d"
strange_format_string = "%m/%d/%Y"

start = datetime.strptime('2016-03-01', normal_format_string)
end = datetime.strptime('2026-02-01', normal_format_string)

strange_format_string = [corporate_bond_spread, market_rates]
normal_format_string = [FRED_yield_spread, unemployment]

for dataset in strange_format_string:
    print("original shape", dataset.shape)
    dataset['observation_date'] = pd.to_datetime(dataset['observation_date'])
    dataset = dataset[(dataset['observation_date'] >= start and dataset['observation_date'] <= end)]

    print("after shape", dataset.shape)
# print(type(market_rates['observation_date'].iloc[0]))
# print(type(datetime.strptime(market_rates['observation_date'].iloc[1], strange_format_string)))
