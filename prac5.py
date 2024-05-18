# Write a program to fill a polygon using Scan line fill algorithm.

def scan_line_fill(x1, y1, x2, y2, x3, y3):
    # Calculate the slope of the lines
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y3 - y2) / (x3 - x2)
    m3 = (y1 - y3) / (x1 - x3)

    # Calculate the y-intercepts
    b1 = y1 - m1 * x1
    b2 = y2 - m2 * x2
    b3 = y3 - m3 * x3

    # Initialize the fill color
    fill_color = True

    # Iterate over each pixel in the scan line
    for y in range(int(min(y1, y2, y3)), int(max(y1, y2, y3)) + 1):
        # Calculate the x-coordinates of the intersection points
        x1_int = int((y - b1) / m1)
        x2_int = int((y - b2) / m2)
        x3_int = int((y - b3) / m3)

        # Determine the fill color based on the intersection points
        if x1_int <= x2_int <= x3_int or x3_int <= x2_int <= x1_int:
            fill_color = True
        elif x2_int <= x1_int <= x3_int or x3_int <= x1_int <= x2_int:
            fill_color = True
        else:
            fill_color = False

        # Draw the pixel if it's within the polygon
        if fill_color:
            print(f"Drawing pixel at ({x1_int}, {y})")

# Example usage
scan_line_fill(0, 0, 3, 3, 2, 2)