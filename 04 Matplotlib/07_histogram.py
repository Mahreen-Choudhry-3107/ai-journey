# plt.hist(data, bins=number_of_bins, color='color_name', edgecolor= 'black')
import matplotlib.pyplot as plt

score= [45, 66, 89, 76, 90, 12, 55, 59, 46, 67, 99, 78, 65, 87]

plt.hist(score, bins=5, color='purple', edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('No. of Students')
plt.title('Score Distribution of students')
plt.show()
           