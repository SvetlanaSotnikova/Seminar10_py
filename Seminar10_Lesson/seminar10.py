# Задача №63. Решение в группах
# 1. Изобразите отношение households к population с
# помощью точечного графика
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

# Чтобы подключить датасет с
# пингвинами, воспользуйтесь данным
# скриптом:
# penguins = sns.load_dataset("penguins")
# penguins.head()

# Библиотека для работы с табличными данными
import pandas as pd
# Библиотека для вычислений линейной алгебры
import numpy as np
# Библиотеки для визуализации
import seaborn as sns
import matplotlib.pyplot as plt

# Начнем с чтения csv данных
df = pd.read_csv('sample_data/california_housing_train.csv')
# Первые пять строк
df.head()

# Изобразите отношение households к population
sns.scatterplot(data=df, x="households", y="population")
sns.scatterplot(data=df, x="households", y="population", hue="total_rooms", size="total_rooms")

# Визуализировать longitude по отношения к median_house_value, используя линейный график
sns.relplot(x="latitude", y="median_house_value", kind="line", data=df, aspect=2, height=7)
# Визуализировать longitude по отношения к median_house_value, используя линейный график
plt.figure(figsize=(16, 8))
sns.lineplot(data=df, x="latitude", y="median_house_value")

# Представить гистограмму по housing_median_age
plt.figure(figsize=(16, 8))
sns.histplot(data=df, x='housing_median_age', bins=50)
plt.title("housing_median_age")
plt.xlabel("media")
plt.ylabel("count")
plt.xticks(range(0,55))
plt.yticks(range(0,1500,40))
plt.grid()

# Изобразить гистограмму по median_house_value с оттенком housing_median_age
plt.figure(figsize=(12, 8))
sns.histplot(data=df, x='median_house_value', hue='housing_median_age', bins=30)


# Задача №65. Решение в группах
# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы





# Задача №67. Решение в группах
# 1. Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)




# Задача №69. Решение в группах
# 1. Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ
