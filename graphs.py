import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as py

data = pd.read_csv('SPX.csv')
df = pd.DataFrame(data)

df['Daily Return'] = df['Close'].pct_change() * 100
df = df.dropna()

sns.set(style='whitegrid')
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Volume', y='Daily Return', data=df, edgecolor=None, hue='Daily Return')
plt.title('Volume vs. Daily Price Change of the S&P 500 Index')
plt.xlabel('Volume')
plt.ylabel('% Change')

plt.show()
