# Write a program to clip a line using Cohen and Sutherland line clipping algorithm.

def encode(x, y, xmin, ymin, xmax, ymax):
    """
    Encode a point based on its position relative to the clipping rectangle.
    """
    code = 0
    if x < xmin:
        code |= 1
    elif x > xmax:
        code |= 2
    if y < ymin:
        code |= 4
    elif y > ymax:
        code |= 8
    return code

def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    """
    Clip a line using the Cohen-Sutherland algorithm.
    """
    code1 = encode(x1, y1, xmin, ymin, xmax, ymax)
    code2 = encode(x2, y2, xmin, ymin, xmax, ymax)
    
    while True:
        if code1 == 0 and code2 == 0:
            # Both endpoints are inside the clipping rectangle
            return x1, y1, x2, y2
        elif code1 & code2 != 0:
            # Both endpoints are outside the clipping rectangle on the same side
            return None, None, None, None
        else:
            # One endpoint is inside, and the other is outside
            # Find the intersection point
            x, y = None, None
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            
            if code_out & 8:
                # Point is above the rectangle
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & 4:
                # Point is below the rectangle
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & 2:
                # Point is to the right of rectangle
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & 1:
                # Point is to the left of rectangle
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            
            if code_out == code1:
                x1, y1 = x, y
                code1 = encode(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = encode(x2, y2, xmin, ymin, xmax, ymax)

# Example usage
xmin, ymin = 0, 0
xmax, ymax = 10, 10

# Line 1: Fully inside the clipping rectangle
x1, y1, x2, y2 = cohen_sutherland(2, 2, 8, 8, xmin, ymin, xmax, ymax)
print(f"Line 1: ({x1}, {y1}) - ({x2}, {y2})")

# Line 2: Fully outside the clipping rectangle
x1, y1, x2, y2 = cohen_sutherland(-2, -2, -8, -8, xmin, ymin, xmax, ymax)
print(f"Line 2: ({x1}, {y1}) - ({x2}, {y2})")

# Line 3: Partially inside the clipping rectangle
x1, y1, x2, y2 = cohen_sutherland(2, 2, 12, 12, xmin, ymin, xmax, ymax)
print(f"Line 3: ({x1}, {y1}) - ({x2}, {y2})")