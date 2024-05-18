# Write a program to draw Hermite /Bezier curve.

from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

# Define the control points
control_points = np.array([[0, 0], [0, 100], [100, 100], [100, 0]])

# Define the Hermite/Bezier curve parameters
num_points = 100
t = np.linspace(0, 1, num_points)

# Calculate the curve points
curve_points = []
for i in range(num_points):
    t_i = t[i]
    p0 = control_points[0]
    p1 = control_points[1]
    p2 = control_points[2]
    p3 = control_points[3]
    curve_point = (
        p0[0] * (1 - t_i)**3 + 3 * p1[0] * (1 - t_i)**2 * t_i + 3 * p2[0] * (1 - t_i) * t_i**2 + p3[0] * t_i**3,
        p0[1] * (1 - t_i)**3 + 3 * p1[1] * (1 - t_i)**2 * t_i + 3 * p2[1] * (1 - t_i) * t_i**2 + p3[1] * t_i**3
    )
    curve_points.append(curve_point)

# Create an image
img = Image.new('RGB', (200, 200), color='white')
draw = ImageDraw.Draw(img)

# Draw the curve
draw.line(curve_points, fill='blue', width=2)

# Display the image
plt.imshow(np.asarray(img))
plt.axis('off')  # Turn off axis
plt.show()