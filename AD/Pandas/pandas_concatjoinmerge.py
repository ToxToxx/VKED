import pandas as pd

raw_data = {
    'subject_id' : ['1', '2', '3', '4' , '5'],
    'first_name' : ['Sasha', 'Dima', 'Ivan', 'Gosha', 'Matvei'],
    'last_name' : ['Gribkov', 'Andreev', 'Lavrov', 'Petrov', 'Popov'],
}

df_a = pd.DataFrame(raw_data, 
                    columns = ['subject_id', 'first_name', 'last_name'])
df_a.index = [0,1,2,3,4]
print('Первый\n', df_a)

raw_data = {
    'subject_id' : ['4', '5', '6', '7' , '8'],
    'first_name' : ['George', 'Alan', 'Andrew', 'Billy', 'Matt'],
    'last_name' : ['Milligan', 'Smith', 'Land', 'Petro', 'Peace'],
}
df_b = pd.DataFrame(raw_data, 
                    columns = ['subject_id', 'first_name', 'last_name'])
df_b.index = [2,3,4,5,6]
print('Второй\n', df_b)

raw_data = {
    'subject_id' : ['1', '2', '3', '4' , '5',  '7','8','9','10','11'],
    'test_id' : [51, 15, 15, 61, 16, 14, 15, 1, 61, 16],
}
df_n = pd.DataFrame(raw_data, 
                    columns = ['subject_id', 'test_id'])
print('Третий\n', df_n)

df_new = pd.concat([df_a, df_b], axis = 0)
print("Конкатенация по строкам\n", df_new)

df_new_ = pd.concat([df_a, df_b], axis = 1)
print('Конкатенация по столбцам\n', df_new_)

df_new_ = pd.concat([df_a, df_b], axis = 1, join = 'inner')
print('Inner join\n ', df_new_)


print('Outer Join\n', df_a._append(df_b))

print('Left join\n', df_a.join(df_b, rsuffix= '_right_table', how = 'left'))

print('Merge\n', pd.merge(df_new, df_n, on = 'subject_id'))

print('Merge left_on right_on\n', pd.merge(df_new, df_n, left_on = 'subject_id', right_on = 'subject_id'))

print('Merge left\n', pd.merge(df_a, df_b, on = 'subject_id', how = 'left'))

print('Merge right\n', pd.merge(df_a, df_b, on = 'subject_id', how = 'right'))

print('Merge index\n', pd.merge(df_a, df_b, right_index = True, left_index = True))
