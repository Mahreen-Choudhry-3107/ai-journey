# savefig('filename.extension', dpi = value, bbox_inches = 'tighti')
import matplotlib.pyplot as plt

x = [1,2,3,4]
y= [10,20,30,40]

# create plot
plt.plot(x,y, color = 'blue', marker = 'o')
plt.title('Simple line plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.savefig('Line_plot.png', dpi=300, bbox_inches='tight')
plt.show()