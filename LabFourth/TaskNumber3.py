import matplotlib.pyplot as plt

# Data about language percentage using in project
categories = ['c#', 'react', 'php', 'javascript', 'entity framework']
values = [20, 25, 15, 30, 10]  #проценты

# Построение круговой диаграммы
plt.figure(figsize=(6, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)

#title
plt.title('Language percentage using in project')

plt.show()
