import random 
import pandas as pd

lst = ['robot'] * 10 
lst += ['human'] * 10 
random.shuffle(lst) 
data = pd.DataFrame({'whoAmI':lst}) 

# Создание one-hot матрицы
unique_values = data['whoAmI'].unique()
one_hot_matrix = pd.DataFrame(0, index=data.index, columns=unique_values)

# Заполнение one-hot матрицы
for i, value in enumerate(data['whoAmI']):
    one_hot_matrix.loc[i, value] = 1

print(one_hot_matrix.head())


