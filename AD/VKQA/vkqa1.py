import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

incomes =  pd.read_excel("E:/Programming/VKED/AD/VKQA/table1.xlsx")
print(incomes.tail())
print(incomes.shape)

currencies = pd.read_excel("E:/Programming/VKED/AD/VKQA/table2.xlsx")
print(currencies.tail())

#Вывести максимальный перевод от 8 февраля в USD
incomes['operation_date'] = pd.to_datetime(incomes['operation_date']) #потому что первоначально не дата
incomes['operation_day'] = incomes['operation_date'].dt.floor('d')

answer1 = incomes[
    (incomes['operation_day'] >= pd.Timestamp('2023-02-08')) 
    & (incomes['currency'] == 'USD')]['volume'].max()
print('First answer', answer1)

#выведите средний размер попонений за февраль подневно, в разбивке по валютам
#Результат - таблица формата дата валюта и размер пополнения с округлением до целого числа
answer2 = incomes.groupby(['operation_day', 'currency']).agg({'volume': np.mean}).reset_index()
print('Second \n', answer2)