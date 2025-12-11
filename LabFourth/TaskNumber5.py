import matplotlib.pyplot as plt

# Data about language percentage using in project
categories = ['c#', 'react', 'php', 'javascript', 'entity framework']
values = [20, 25, 15, 30, 10]  #проценты

#строим столбчатую диаграмму
plt.figure(figsize=(8, 5))
plt.barh(categories, values, color='skyblue')

plt.title('Language percentage using in project')
plt.xlabel('values')
plt.ylabel('technologies')

#сетка
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()
