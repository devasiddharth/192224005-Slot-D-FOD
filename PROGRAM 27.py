import numpy as np
revenue=[100,120,150,130,110,140,120,130,110,120]
mean=np.mean(revenue)
std_dev=np.std(revenue)
confidence_level=0.95
z_alpha=1.96
margin_of_error=z_alpha*std_dev/np.sqrt(len(revenue))
lower_bound=mean - margin_of_error
upper_bound=mean + margin_of_error
print("Confidence interval for mean revenue at 95% confidence level:")
print(f"Lower bound:{lower_bound:.2f}")
print(f"Upper bound:{upper_bound:.2f}")
