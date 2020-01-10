# 15-1 & 15-2 plot cubes graph
import matplotlib.pyplot as plt

x_values = range(1,6)
y_values = [x**3 for x in x_values]
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, s=5)
# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.axis([0,6,0,150])
plt.show()

# plot the first 5000 cubic numbers
x_values = range(0, 5000)
y_values = [x**3 for x in x_values]
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, s=2)
# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.axis([0,5010,0,126000000000])
plt.show()