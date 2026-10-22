# plt.subplot(nrows, ncols, index)
import matplotlib.pyplot as plt

x = [1,2,3,4]
y= [10, 20, 15, 25]

plt.subplot(1,2,1)  #1 row, 2column, at 1st pos 
plt.plot(x,y)
plt.title('Line chart')

plt.subplot(1,2,2) #1row, 2nd col, 2nd subplot
plt.bar(x,y)
plt.title('Bar chart')

plt.tight_layout()
plt.show


# professional way
import matplotlib.pyplot as plt

# fig, ax = plt.subplots, ncols, figsize=(w, h))
fig, ax, = plt.subplots(1,2, figsize = (10,5))

x = [1,2,3,4]
y = [10, 20, 15, 25]

ax[0].plot(x, y)
ax[0].set_title('Line Plot')

ax[1].bar(x,y)
ax[1].set_title('Bar Chart')

plt.tight_layout()
plt.show()

# customize colors etc


import matplotlib.pyplot as plt

# fig, ax = plt.subplots, ncols, figsize=(w, h))
fig, ax, = plt.subplots(1,2, figsize = (10,5))

x = [1,2,3,4]
y = [10, 20, 15, 25]

ax[0].plot(x, y, color='blue')
ax[0].set_title('Line Plot')

ax[1].bar(x,y, color='green')
ax[1].set_title('Bar Chart')

fig.suptitle('Comparison of Line and Bar Chart')

plt.tight_layout()
plt.show()