import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
df=pd.DataFrame({
    'age':[22,25,28,30,32,35,37,39,42,44,46,48,50,52,54,56,58,60],
    '%fat':[18,22,25,27,29,32,34,36,38,40,42,44,46,48,50,52,54,56]})
print("Mean of age:",df['age'].mean())
print("Median of age:",df['age'].median())
print("Standard deviation of age :",df['age'].std())
print("Mean of %fat:",df['%fat'].mean())
print("Median %fat:",df['%fat'].median())
print("Standard deviation of %fat :",df['%fat'].std())
df.boxplot(column=['age','%fat'])
plt.show()
plt.scatter(df['age'],df['%fat'])
plt.xlabel("Age")
plt.ylabel("%fat")
plt.title("Scatter plot of Age vs %fat")
plt.show()
stats.probplot(df['%fat'],plot=plt)
plt.xlabel("%fat")
plt.ylabel('Theoretical quantities')
plt.title('Q-Q plot of %fat')
plt.show()
