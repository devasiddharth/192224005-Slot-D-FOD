import matplotlib.pyplot as plt
import pandas as pd
data={
    'study_time':[4,6,5,8,2,7,3,1],
    'exam_scores':[76,82,78,93,68,89,65,54]}
df=pd.DataFrame(data)
correlation_coefficient=df['study_time'].corr(df['exam_scores'])
print("Correlation coefficient :",correlation_coefficient)
plt.scatter(df['study_time'],df['exam_scores'])
plt.xlabel('Study Time(Hours)')
plt.ylabel('Exam Scores')
plt.title("Scatterplot:Study Time vs Exam Scores")
plt.show()
plt.plot(df['study_time'],df['exam_scores'])
plt.xlabel('Study Time(Hours)')
plt.ylabel('Exam Scores')
plt.title("Lineplot:Study Time vs Exam Scores")
plt.show()
plt.hist(df['exam_scores'],bins=5,edgecolor='black')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title("Histogram:Study Time vs Exam Scores")
plt.show()



 

