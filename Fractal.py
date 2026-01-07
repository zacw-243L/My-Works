import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Function to generate the Sierpiński triangle points
def sierpinski_triangle(num_points):
    vertices = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2.0]])
    points = np.zeros((num_points, 2))
    points[0] = np.random.rand(2)
    for i in range(1, num_points):
        chosen_vertex = vertices[np.random.randint(0, 3)]
        points[i] = (points[i - 1] + chosen_vertex) / 2
    return points

# Function to update the animation
def update(frame):
    global zoom, ax
    zoom /= 1.02
    ax.clear()
    ax.axis('off')
    ax.set_xlim(0.5 - zoom, 0.5 + zoom)
    ax.set_ylim(np.sqrt(3) / 4 - zoom / 2, np.sqrt(3) / 4 + zoom / 2)
    points = sierpinski_triangle(num_points)
    ax.scatter(points[:, 0], points[:, 1], s=0.1, color='blue')
    return ax,

# Measure performance and set zoom limits
def measure_performance():
    global zoom, ax, fig, num_points
    start_time = time.time()
    try:
        ani = animation.FuncAnimation(fig, update, frames=range(1000), interval=50, blit=True)
        plt.show()
    except MemoryError as e:
        print(f"MemoryError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    end_time = time.time()
    print(f"Zoomed in for {end_time - start_time:.2f} seconds before encountering issues.")

# Parameters
num_points = 100000  # Number of points to generate for the Sierpiński triangle
zoom = 2.0  # Initial zoom level

# Set up figure
fig, ax = plt.subplots()
ax.set_xlim(0.5 - zoom, 0.5 + zoom)
ax.set_ylim(np.sqrt(3) / 4 - zoom / 2, np.sqrt(3) / 4 + zoom / 2)
ax.axis('off')

# Measure performance
measure_performance()
