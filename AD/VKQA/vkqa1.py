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

#посчитать долю клиентов,у которых были пополнения в нескольких валютах. Округлить до десятых процента
users_currencies_count = incomes.groupby('user_id')['currency'].nunique().reset_index()
sum_of_all_currencies_bigger1 = sum(users_currencies_count['currency'] > 1)
unique_users = incomes['user_id'].nunique()
answer3 = round((sum_of_all_currencies_bigger1 / unique_users * 100), 1)
print('Third ', answer3)

#по каждому клиенту вывести дату первого пополнения
#валюту,сумму в рублях(использовать вторую таблицу)
#Ответом вывести общую сумму в рублях по всем клиентам

#1 -найти для каждого клиента запись с самым первым пополнением
users_first_income = incomes.groupby('user_id')['operation_date'].min().reset_index()
merging_incomes_firstIncome = pd.merge(incomes, users_first_income, 'inner', ['user_id', 'operation_date'])

#2 - джоин таблиц с пополнениями и с курсами валют
currencies.loc[currencies['rate_currency'] == 'CNY', 'rate_value'] = currencies.loc[currencies['rate_currency'] == 'CNY', 'rate_value'].apply(lambda x: str(x)[5:7] + '.' + str(x)[:4])
currencies['rate_value'] = currencies['rate_value'].astype(float)

#3 - нужно вывести сумму в рублях
first_incomes_with_rate_values = pd.merge(merging_incomes_firstIncome, 
         currencies, 
         how = 'left', 
         left_on = ['currency', 'operation_day'], 
         right_on = ['rate_currency', 'rate_date'])

first_incomes_with_rate_values['rate_value'] = first_incomes_with_rate_values['rate_value'].fillna(1.0)
answer4 = sum(first_incomes_with_rate_values['volume'] * first_incomes_with_rate_values['rate_value'])

print('Fourth', answer4)