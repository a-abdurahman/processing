size(800, 800)
background(0, 0, 50)

xx = 2
yy = xx+2

for x1 in range(xx):
     stroke(255, 255, 255)
     line(420 + x1 * 20, 400, 420 + x1 * 20, 380)
     line(400, 390, 420 + x1 * 20, 390)
     
for y1 in range(xx):
     stroke(255, 255, 255)
     line(410, 370 - y1 * 20, 390, 370 - y1 * 20)
     line(400, 390, 400, 370 - y1 * 20)
     
for x2 in range(yy):
     stroke(255, 255, 255)
     line(420 - x2 * 20, 400, 420 - x2 * 20, 380)
     line(400, 390, 420 - x2 * 20, 390)
     
for y2 in range(yy):
     stroke(255, 255, 255)
     line(410, 370 + y2 * 20, 390, 370 + y2 * 20)
     line(400, 390, 400, 370 + y2 * 20)
