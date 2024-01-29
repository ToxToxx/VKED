import pandas as pd
import numpy as np

df = pd.read_csv("E:/Programming/VKED/AD/Pandas/orders.csv")

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.precision', 3)


print('     Tail\n', df.tail())
print('     Head\n', df.head())

print('     Shape ', df.shape)
print('     Columns', df.columns)
print('     Describe\n', df.describe())
print('     Describe object\n', df.describe(include=['object']))
print('     City id count\n', df.city_id.value_counts(dropna = False)[:10])
print(df.info())

for dtype in ['float', 'int', 'object']:
    selected_dtype = df.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep = True).mean()
    mean_usage_mb = mean_usage_b / 1024 ** 2
    print('Среднее использование памяти для {} столбца: {:03.2f} MB'.format(dtype, mean_usage_mb))

df['fail_orders'] = df['fail_orders'].astype('int32')
print(df.info())

#тип данных КАТЕГОРИЯ
print([(col, df[col].nunique()) for col in df.columns])

unique_counts = pd.DataFrame.from_records([(col, df[col].nunique()) for col in df.columns],
                                          columns = ['Column_name', 'Num_unique']).sort_values(by = ['Num_unique'])

print(unique_counts)

df_with_cat = df.copy()

df_with_cat['vendor_id'] = df_with_cat['vendor_id'].astype('category')

print(df_with_cat.info())

#ускорение сравнительно с df - 5 раз

#Сортировка
print('     Сортировка\n', df.sort_values(by = ['vendor_id', 'successful_orders'],
                     ascending = [True,False]).head(5))


print('     ILOC\n', df.iloc[:, 0:4])

print('Mean ', df[df['vendor_id'] == 40065]['successful_orders'].mean())
print('Min ', df[df['vendor_id'] == 40065]['successful_orders'].min())