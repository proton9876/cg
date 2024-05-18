# Write a program to apply various 3D transformations on a 3D object and then apply
# parallel and perspective projection on it.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the 3D object (a cube)
vertices = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
])

edges = np.array([
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
])

# Define the transformations
def translate(vertices, x, y, z):
    return vertices + np.array([x, y, z])

def scale(vertices, x, y, z):
    return vertices * np.array([x, y, z])

def rotate(vertices, angle, axis):
    if axis == 'x':
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle), -np.sin(angle)],
            [0, np.sin(angle), np.cos(angle)]
        ])
    elif axis == 'y':
        rotation_matrix = np.array([
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ])
    elif axis == 'z':
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]
        ])
    return np.dot(vertices, rotation_matrix)

# Apply transformations
vertices = translate(vertices, 1, 1, 1)
vertices = scale(vertices, 2, 2, 2)
vertices = rotate(vertices, np.pi/4, 'z')

# Apply parallel projection
parallel_projection = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
vertices_parallel = np.dot(vertices, parallel_projection)

# Apply perspective projection
def perspective_projection(vertices):
    d = 2  # Distance from the viewer to the projection plane
    perspective_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1/d],
        [0, 0, 0, 0]
    ])
    homogeneous_vertices = np.concatenate((vertices, np.ones((vertices.shape[0], 1))), axis=1)
    projected_vertices = np.dot(homogeneous_vertices, perspective_matrix.T)
    projected_vertices = projected_vertices[:, :3] / projected_vertices[:, 3][:, None]
    return projected_vertices

vertices_perspective = perspective_projection(vertices)


# Plot the 3D object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='r')
ax.scatter(vertices_parallel[:, 0], vertices_parallel[:, 1], vertices_parallel[:, 2], c='g')
ax.scatter(vertices_perspective[:, 0], vertices_perspective[:, 1], vertices_perspective[:, 2], c='b')
plt.show()