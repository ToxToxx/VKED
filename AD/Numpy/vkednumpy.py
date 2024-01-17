import numpy as np

#ndarray - быстрый и гибкий контейнер для хранения больших данных на python, многомерный массив
#ndarray.ndim - число осей массива
#ndarray.shape - размеры массива, его форма
#ndarray.size - число всех элементов массива
#ndarray.dtype - объект описывающий тип элементов массива
#ndrarray.itemsize - размер каждого элемента в байтах
#ndarray.data - буфер с фактическими элементами массива

#основные операции
data1 = [ [1.2, 3.6, 7.1], [4.1, 0.6, 5.76]]
arr1 = np.array(data1)
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(arr1.itemsize)
print(arr1.data)

data_zeros = np.zeros(5)
print(data_zeros)

data_ones = np.ones((2,2))
print(data_ones)

data_arange = np.arange(10)
print(data_arange)

data_linspace = np.linspace(0, 2, 15)
print(data_linspace)

data_eye = np.eye(3)
print(data_eye)

#операции между массивами и скалярами
print("         ОПЕРАЦИИ            Ы")
example_array = np.array([[1.,2.,3.], [4.,5.,6.]])
print("1", example_array * example_array)
print("2", example_array - example_array)
print("3", 1 / example_array)