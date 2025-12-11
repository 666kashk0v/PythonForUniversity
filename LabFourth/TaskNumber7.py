import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  #для работы с 3д

#генерим данные
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

#cтроим график
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#настройки поверхности
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

#set color
fig.colorbar(surf, shrink=0.5, aspect=5, label='z = sin(sqrt(x^2 + y^2))')

# Настройки осей
ax.set_title('3D Graph')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
