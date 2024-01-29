import pandas as pd

raw_data = {
    'subject_id' : ['1', '2', '3', '4' , '5'],
    'first_name' : ['Sasha', 'Dima', 'Ivan', 'Gosha', 'Matvei'],
    'last_name' : ['Gribkov', 'Andreev', 'Lavrov', 'Petrov', 'Popov'],
}

df_a = pd.DataFrame(raw_data, 
                    columns = ['subject_id', 'first_name', 'last_name'])
df_a.index = [0,1,2,3,4]
print(df_a)

raw_data = {
    'subject_id' : ['4', '5', '6', '7' , '8'],
    'first_name' : ['George', 'Alan', 'Andrew', 'Billy', 'Matt'],
    'last_name' : ['Milligan', 'Smith', 'Land', 'Petro', 'Peace'],
}
df_b = pd.DataFrame(raw_data, 
                    columns = ['subject_id', 'first_name', 'last_name'])
df_b.index = [2,3,4,5,6]
print(df_b)

raw_data = {
    'subject_id' : ['1', '2', '3', '4' , '5',  '7','8','9','10','11'],
    'test_id' : [51, 15, 15, 61, 16, 14, 15, 1, 61, 16],
}
df_n = pd.DataFrame(raw_data, 
                    columns = ['subject_id', 'test_id'])
print(df_n)