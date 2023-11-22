# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# попытка 1 без думиеса (все значения одинаковые, не получилось)
# one_hot_columns = pd.unique(data['whoAmI'])
# one_hot = pd.DataFrame(0, columns=one_hot_columns, index=data.index)

# one_hot.loc[data.index, data['whoAmI']] = 1
# data = pd.concat([data, one_hot], axis=1)

# data = data.drop('whoAmI', axis=1)
# print(data.head())

# вторая попытка без думиеса (вроде получилось)
unique_values = data['whoAmI'].unique()

# Создание one-hot кодировки
for value in unique_values:
    data[f'{value}'] = (data['whoAmI'] == value).astype(int)

data = data.drop('whoAmI', axis=1)

print(data.head())


# использоавние думиеса
# one_hot = pd.get_dummies(data['whoAmI']) # prefix='WhoAmI'
# one_hot = one_hot.astype(int)
# # Объединение исходного DataFrame с one-hot кодировкой
# data = pd.concat([data, one_hot], axis=1)

# data = data.drop('whoAmI', axis=1)

# print(data.head())
