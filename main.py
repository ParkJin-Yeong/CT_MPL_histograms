import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

median_age = 29
color = '#fc4f30'

bins = list(range(10, 101, 10))
plt.hist(ages, bins=bins, edgecolor='black', log=True)

plt.axvline(median_age, color=color, label="Age Median", linewidth=2)
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()