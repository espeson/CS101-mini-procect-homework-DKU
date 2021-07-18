import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

air = pd.read_csv('air.csv')




air.plot(x = 'num', y = 'PM2.5')
plt.xlabel('number of date')
plt.ylabel('PM 2.5')

plt.show()