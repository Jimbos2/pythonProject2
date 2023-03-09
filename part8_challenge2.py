import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('1.supermarket.csv')

q = data.groupby('item_name').quantity.sum()

plt.bar(q.index, q,
        color=['orange', 'purple', 'yellow', 'red', 'green', 'blue', 'cyan'])
plt.xlabel('Items')
plt.xticks(rotation=6)
plt.ylabel('Number of Times Ordered')
plt.title('Most ordered Supermaket\'s Items')
plt.show()
