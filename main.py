import csv
import pandas as pd
import datetime as dt


corporate_bond_spread = pd.read_csv('data/corporate_bond_spread_csv.csv') #Header: {Date, Value} Shape: (7634, 2) 
corporate_bond_spread = corporate_bond_spread.rename(columns={'Date': 'observation_date'})

FRED_yield_spread = pd.read_csv('data/FRED_high_yield_index_spread_csv.csv') #Header: {observation_date, BAMLH0A0HYM2} Shape: (2644, 2) Start Date: 2016-03-30
unemployment = pd.read_csv('data/unemployment_csv.csv') #Header: {observation_date, UNRATE} #Shape: (120, 2) Start date: 2016-03-01

market_rates = pd.read_csv('data/fed_funds_rate_csv.csv') 


'''Index(['Effective Date', 'Rate Type', 'Rate (%)', '1st Percentile (%)',
       '25th Percentile (%)', '75th Percentile (%)', '99th Percentile (%)',
       'Volume ($Billions)', 'Target Rate From (%)', 'Target Rate To (%)',
       'Intra Day - Low (%)', 'Intra Day - High (%)', 'Standard Deviation (%)',
       '30-Day Average SOFR', '90-Day Average SOFR', '180-Day Average SOFR',
       'SOFR Index', 'Revision Indicator (Y/N)', 'Footnote ID'],
      dtype='str')

      Shape: (11051, 19)

      '''

#Feature Engineering
data = [corporate_bond_spread, FRED_yield_spread, unemployment, market_rates]

for dataset in data:
    pass

