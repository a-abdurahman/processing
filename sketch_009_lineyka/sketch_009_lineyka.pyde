from func import *

size(800, 800)
background(255, 255, 255)

cell()

scale1 = 5  
for x1 in range(scale1):
    for y1 in range(scale1):
        stroke(0, 0, 0)
        line(420 + x1 * 20, 400, 420 + x1 * 20, 380)
        line(400, 390, 420 + x1 * 20, 390)
        line(380 - x1 * 20, 400, 380 - x1 * 20, 380)
        line(400, 390, 380 - x1 * 20, 390)
        line(410, 370 - y1 * 20, 390, 370 - y1 * 20)
        line(400, 390, 400, 370 - y1 * 20)
        line(410, 410 + y1 * 20, 390, 410 + y1 * 20)
        line(400, 390, 400, 410 + y1 * 20)

     
