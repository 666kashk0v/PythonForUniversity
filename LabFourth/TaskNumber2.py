import numpy as np
import matplotlib.pyplot as plt

#создание кластеров
x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

x2 = np.random.normal(4, 0.5, 50)
y2 = np.random.normal(4, 0.5, 50)

x3 = np.random.normal(6, 0.5, 50)
y3 = np.random.normal(1, 0.5, 50)

# построение диаграммы
plt.figure(figsize=(8, 6))
plt.scatter(x1, y1, color='red', label='cluster1')
plt.scatter(x2, y2, color='blue', label='cluster2')
plt.scatter(x3, y3, color='green', label='cluster3')

#доп настройки
plt.title('Точечная диаграмма с тремя кластерами')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

plt.show()
