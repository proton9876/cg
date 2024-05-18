# Write a program to apply various 2D transformations on a 2D object (use homogenous Coordinates).

import numpy as np
import matplotlib.pyplot as plt

# Define the 2D object (a square)
vertices = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Define the transformations
def translate(vertices, tx, ty):
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    return np.dot(vertices, translation_matrix.T)

def scale(vertices, sx, sy):
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    return np.dot(vertices, scaling_matrix.T)

def rotate(vertices, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    return np.dot(vertices, rotation_matrix.T)

# Apply transformations
vertices_translated = translate(vertices, 1, 1)
vertices_scaled = scale(vertices, 2, 2)
vertices_rotated = rotate(vertices, np.pi/4)

# Plot the original and transformed 2D objects
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.plot(np.append(vertices[:, 0], vertices[0, 0]), np.append(vertices[:, 1], vertices[0, 1]), 'r-')
plt.title('Original Object')
plt.axis('equal')

plt.subplot(132)
plt.plot(np.append(vertices_translated[:, 0], vertices_translated[0, 0]), np.append(vertices_translated[:, 1], vertices_translated[0, 1]), 'g-')
plt.title('Translated Object')
plt.axis('equal')

plt.subplot(133)
plt.plot(np.append(vertices_rotated[:, 0], vertices_rotated[0, 0]), np.append(vertices_rotated[:, 1], vertices_rotated[0, 1]), 'b-')
plt.title('Rotated Object')
plt.axis('equal')

plt.show()