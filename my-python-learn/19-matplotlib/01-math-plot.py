import numpy as np
import matplotlib.pyplot as plt

x = np.array([2020, 2021, 2022, 2023])
y = np.array([6.6, 8.7, 4.5, 7.9])

plt.title('Indias GDP by Year')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.grid(color='b', linestyle='--', linewidth=1, axis='y')
plt.plot(x, y, color='Orange')
plt.show()