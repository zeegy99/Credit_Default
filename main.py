import pandas as pd
from datetime import datetime

# --- Load ---
t_bill_10y = pd.read_csv('data/DGS10.csv')
t_bill_2y = pd.read_csv('data/DGS2.csv')
b_a = pd.read_csv('data/BAA_AAA.csv')

# --- Convert to numeric (handles FRED's "." missing values) ---
t_bill_10y['DGS10'] = pd.to_numeric(t_bill_10y['DGS10'], errors='coerce')
t_bill_2y['DGS2'] = pd.to_numeric(t_bill_2y['DGS2'], errors='coerce')
b_a['BAA_AAA'] = pd.to_numeric(b_a['BAA_AAA'], errors='coerce')

# --- Standardize dates ---
for df in [t_bill_10y, t_bill_2y, b_a]:
    df['observation_date'] = pd.to_datetime(df['observation_date'])

# --- Filter date range ---
start = pd.Timestamp('1962-01-02')
end = pd.Timestamp('2026-03-01')

t_bill_10y = t_bill_10y[(t_bill_10y['observation_date'] >= start) & (t_bill_10y['observation_date'] <= end)]
t_bill_2y  = t_bill_2y[ (t_bill_2y['observation_date']  >= start) & (t_bill_2y['observation_date']  <= end)]
b_a        = b_a[       (b_a['observation_date']        >= start) & (b_a['observation_date']        <= end)]

# --- Merge everything on date ---
df = pd.merge(t_bill_10y, t_bill_2y, on='observation_date')
df = pd.merge(df, b_a, on='observation_date')

# --- Build features ---
df['10Y-2Y_spread']    = df['DGS10'] - df['DGS2']
df['Premium_BBB_Spread'] = df['BAA_AAA']

# --- Drop NaNs ---
df = df.dropna()

print(df.shape)
print(df.head())
