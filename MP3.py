from graphics import *
import random


win = GraphWin('Image Manipulation', 1280, 720)
def blur(filename):
    img = Image(Point(640,360),filename)
    for x in range(1280):
        for y in range(720):
            a = random.random()
            if a<=0.5:
                continue
            else:
                list=[]
                rows = 720
                cols = 1280
                for i in range(-5, 6):
                    if x + i < 0 or x + i >= cols:
                        continue
                    for j in range(-5, 6):
                        if y + j < 0 or y + j >= rows:
                            continue
                        if i == 0 and j == 0:
                            continue
                        else:
                            list.append(img.getPixel(x+i, y+j))
                color=random.choice(list)
                r=color[0]
                g=color[1]
                b=color[2]
                img.setPixel(x,y,color_rgb(r,g,b))
    img.draw(win)
    img.save("xc166_blurred.gif")
blur("source.gif")
def green_screen(filename1, filename2):
    img1 = Image(Point(640, 360), filename1)
    img2 = Image(Point(640, 360), filename2)
    for x in range(1280):
        for y in range(720):
            if img1.getPixel(x,y)[0]==0 and img1.getPixel(x,y)[2]==0:
                r=img2.getPixel(x,y)[0]
                g = img2.getPixel(x, y)[1]
                b = img2.getPixel(x, y)[2]
                img1.setPixel(x,y,color_rgb(r,g,b))
    img1.draw(win)
    img1.save("xc166_componsite.png")
    pass
# green_screen("ironman_greenscreen.gif", "steph_curry.gif")
