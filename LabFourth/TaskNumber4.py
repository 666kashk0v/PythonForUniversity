import numpy as np
import matplotlib.pyplot as plt

#matrix10x10
data = np.random.rand(10, 10)

#температурная карта
plt.figure(figsize=(6, 6))
plt.imshow(data, cmap='viridis', interpolation='nearest')

plt.colorbar(label='value')

# Заголовок
plt.title('Temperature map 10x10 random numbers')

plt.show()
