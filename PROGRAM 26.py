import numpy as np
import matplotlib.pyplot as plt
temperature=[20,22,24,26,28,30,32,34,36,38,40,42]
rainfall=[10,12,14,16,18,20,22,24,26,28,30,32]
mean_temperature=np.mean(temperature)
mean_rainfall=np.mean(rainfall)
deviation_temperature=temperature - mean_temperature
deviation_rainfall=rainfall-mean_rainfall
covariance=np.sum(deviation_temperature * deviation_rainfall)
variance_temperature=np.var(temperature)
variance_rainfall=np.var(rainfall)
correlation_coefficient=covariance/(np.sqrt(variance_temperature)*np.sqrt(variance_rainfall))
print("Correlation coefficient:",correlation_coefficient)
plt.scatter(temperature,rainfall)
plt.xlabel("Temperature")
plt.ylabel("rainfall")
plt.title("Scatterplot of Temperature vs Rainfall")
plt.show()
