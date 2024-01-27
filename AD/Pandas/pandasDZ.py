import pandas as pd
import numpy as np

dz_series = pd.read_csv("E:/Programming/VKED/AD/Pandas/orders.csv")
print(dz_series)
print(dz_series['city_id'].nunique())
sushi_filter = (dz_series.spec == "Суши")
print(len(dz_series[sushi_filter]))
print(dz_series.select_dtypes(include='float64').shape[1])
orders4065 = dz_series[dz_series['vendor_id'] == 40065]
orders_less20 = orders4065[orders4065['successful_orders'] < 20].shape[0]
print(orders_less20)