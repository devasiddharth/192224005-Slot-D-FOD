import pandas as pd
data=[
    {"post_id":1,"likes":25},
    {"post_id":2,"likes":40},
    {"post_id":3,"likes":62},
    {"post_id":4,"likes":20},
    {"post_id":5,"likes":25},
    {"post_id":6,"likes":45},
    {"post_id":7,"likes":62}]
df=pd.DataFrame(data)
frequency_distribution=df['likes'].value_counts()
print(frequency_distribution)
