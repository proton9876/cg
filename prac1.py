# Write a program to implement DDA and Bresenham’s line drawing algorithm.

from PIL import Image, ImageOps
image = Image.new("RGB", size=(50, 50), color=(255,255,255))

def draw_line_dda(image : Image, start_pos, end_pos):
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    # calculate slope
    dx, dy = x2-x1, y2-y1
    m = dy/dx if dx > 0 else float('inf')

    x, y = x1, y1
    image.putpixel((round(x), round(y)), (10, 10, 10, 255))
    
    width, height = image.size

    while True:
        if m <= 1:
            x += 1
            y += m
        else:
            x += (1/m)
            y += 1

        if (x >= x2 or x >= width) or (y >= y2 or y>=height):
            break

        image.putpixel((round(x), round(y)), (10, 10, 10, 255))

def draw_line_bresanham(image: Image, start_pos, end_pos):
    x1, y1 = start_pos
    x2, y2 = end_pos

    dx = x2-x1
    dy = y2-y1

    p = (2*dy) - dx
    m = dy/dx if dx > 0 else float('inf')

    x, y = x1, y1
    image.putpixel((round(x), round(y)), (10, 10, 10, 255))

    width, height = image.size

    while True:
        if m < 1:
            if p < 0:
                x += 1
                p += (2*dy)
            else:
                y += 1
                x += 1
                p += (2*(dy-dx))
        else:
            if p < 0:
                y += 1
                p += (2*dx)
            else:
                y += 1
                x += 1
                p += (2*(dx)-dy)
        

        if (x >= x2 or x >= width) and (y >= y2 or y>=height):
            print((round(x), round(y)))
            break
        image.putpixel((round(x), round(y)), (10, 10, 10, 255))

# draw line
if __name__ == "__main__":     
    # draw_line_bresanham(image, (0,0), (40, 10))
    # draw_line_bresanham(image, (0,0), (40, 20))
    # draw_line_bresanham(image, (0,0), (40, 30))
    # draw_line_bresanham(image, (0,0), (40, 40))

    draw_line_bresanham(image, (10,0), (10, 40))

    ImageOps.flip(image).show()