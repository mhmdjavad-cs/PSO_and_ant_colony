import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

# Define the function to plot
def func(x, y):
    return abs(math.sin(x) * math.cos(y) * math.exp(abs(1 - (math.sqrt(x**2 + y**2))/math.pi)))

# Create x, y data points
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
X, Y = np.meshgrid(x, y)

# Evaluate the function at each x, y point
#Z = abs(math.sin(X) * math.cos(Y) * math.exp(abs(1 - (math.sqrt(X**2 + Y**2))/math.pi)))
#Z = func(X, Y)
# Evaluate the function at each x, y point
Z = np.zeros_like(X)
for i in range(len(x)):
    for j in range(len(y)):
        Z[i,j] = func(x[i], y[j])


# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()


# Set axes label
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('t', labelpad=20)

plt.show()