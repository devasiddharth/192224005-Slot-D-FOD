import numpy as np
data=np.array([2,3,5,4,1,6,7,8])
mean=np.mean(data)
print("Mean:",mean)
variance=np.var(data)
print("Variance:",variance)
sample_size=4
sample=np.random.choice(data,size=sample_size,replace=False)
print("Simple random sample:",sample)
strata=np.unique(data)
stratified_sample=[]
for stratum in strata:
    stratum_data=data[data==stratum]
    sample_size=int(len(stratum_data)*0.25)
    stratified_sample.append(np.random.choice(stratum_data,size=sample_size,replace=False))
stratified_sample=np.concatenate(stratified_sample)
print("Stratified sample:",stratified_sample)
sampling_interval=2
systematic_sample=data[:sampling_interval]
print("Systematic sample:",systematic_sample)
clusters=np.array_split(data,4)
cluster_indices=np.random.choice(4,size=2,replace=False)
cluster_sample=np.concatenate([clusters[i] for i in cluster_indices])
print("Cluster sample:",cluster_sample)
