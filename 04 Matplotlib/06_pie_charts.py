# plt.pie(values, color='color name', label='label-name', autopct='%1.1f%%')
import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West']
revenue = [3000, 2000, 1500, 1000]

plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=['gold', 'skyblue', 'lightgreen', 'coral'])
plt.title('Revenue Contribution By Region')
plt.show()