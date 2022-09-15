import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('liquorstore.csv')
#print(df.head(5))
#print(df.info())
df['zip_code'] = df['zip_code'].astype(int)

aggr_1 = df.groupby('zip_code').bottles_sold.sum()
aggr_2 = df.groupby('store_name').sale_dollars.sum()
print(aggr_1)
print(aggr_2)

df.to_csv('liquorstore2.csv')

#plt.scatter(df['zip_code'], df['bottles_sold'])
#plt.show()
