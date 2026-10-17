# plt.bar(x, height, color='color name', width = value, label='label-name')
import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D']
sales = [1000, 1500, 800, 1200]

plt.bar(product, sales, color='orange', label='Sales 2025')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product Sales Comaprison')
plt.legend()
plt.show()