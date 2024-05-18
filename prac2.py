# Write a program to implement mid-point circle drawing algorithm.

from PIL import Image, ImageOps
image = Image.new("RGB", size=(50, 50), color=(255,255,255))

def draw_circle_mid_point(image : Image, center, r):
    x, y = 0, r
    p = 1-r
    x_c, y_c = center
    
    width, height = image.size

    image.putpixel((x_c, y_c+r), (10, 10, 10, 255))
    image.putpixel((x_c, y_c-r), (10, 10, 10, 255))
    image.putpixel((x_c+r, y_c), (10, 10, 10, 255))
    image.putpixel((x_c-r, y_c), (10, 10, 10, 255))

    while x <= y:
        x += 1
        if p < 0:
            p += (2*x + 1)
        else:
            y -= 1
            p += 2*(x-y) + 1
        
        if (0 <= x+x_c <= width) and (0 <= y+y_c <= height):
            image.putpixel((x+x_c, y+y_c), (10, 10, 10, 255))
            image.putpixel((x+x_c, -y+y_c), (10, 10, 10, 255))
            image.putpixel((-x+x_c, -y+y_c), (10, 10, 10, 255))
            image.putpixel((-x+x_c, y+y_c), (10, 10, 10, 255))

            image.putpixel((y+y_c, x+x_c), (10, 10, 10, 255))
            image.putpixel((y+y_c, -x+x_c), (10, 10, 10, 255))
            image.putpixel((-y+y_c, -x+x_c), (10, 10, 10, 255))
            image.putpixel((-y+y_c, x+x_c), (10, 10, 10, 255))



if __name__ == '__main__':
    draw_circle_mid_point(image, (25, 25), 20)
    ImageOps.flip(image).show()