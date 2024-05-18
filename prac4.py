# Write a program to clip a polygon using Sutherland Hodgeman algorithm.

def clip_polygon(polygon, xmin, ymin, xmax, ymax):
    def inside(p):
        return (xmin <= p[0] <= xmax) and (ymin <= p[1] <= ymax)

    def compute_intersection(p1, p2, edge):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3, x4, y4 = edge
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        
        if denominator != 0:
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
            return (px, py)
        else:
            return None

    clipped_polygon = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        if i == len(polygon) - 1:
            p2 = polygon[0]
        else:
            p2 = polygon[i + 1]

        if inside(p2):
            if not inside(p1):
                clipped_polygon.append(compute_intersection(p1, p2, [xmin, ymin, xmin, ymax]))
            clipped_polygon.append(p2)
        elif inside(p1):
            clipped_polygon.append(compute_intersection(p1, p2, [xmin, ymin, xmin, ymax]))

    return clipped_polygon

# Example usage
polygon = [(0, 0), (2, 0), (2, 2), (0, 2)]
clipped_polygon = clip_polygon(polygon, 1, 1, 3, 3)
print("Original polygon:", polygon)
print("Clipped polygon:", clipped_polygon)