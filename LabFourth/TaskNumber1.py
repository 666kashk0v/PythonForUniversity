import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 100)  # Интервал [0, 5], 100 точек
y1 = np.sin(x)#func1
y2 = np.exp(x)#func2

#фигура и ось
fig, ax1 = plt.subplots()

#функция sin
color = 'tab:blue'
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color=color)
line1, = ax1.plot(x, y1, color=color, label='sin(x)')
ax1.tick_params(axis='y', labelcolor=color)

#функция exp
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('exp(x)', color=color)
line2, = ax2.plot(x, y2, color=color, label='exp(x)')
ax2.tick_params(axis='y', labelcolor=color)

#создание легенды
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left')

ax1.annotate('max sin(x)', xy=(np.pi/2, 1), xytext=(2, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
ax2.annotate('рост exp(x)', xy=(5, np.exp(5)), xytext=(3, 100),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('sin(x) и exp(x)')
plt.show()
