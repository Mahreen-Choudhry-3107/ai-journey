import matplotlib.pyplot as plt
x = ['Mon', 'Tues', 'Wednes', 'Thur', 'Fri']
y = [10, 25, 7, 20, 12]

plt.plot(x, y)

plt.title('Bakery Sales This Week!')

plt.xlabel('Day of the week')
plt.ylabel('Sales per day')

plt.show()