

def setup():
    size(1000, 600)
    
x = 0
y = 0
stepX = 2
stepY = 2
def draw():
    global x, y, stepX, stepY
    background(255)
    x += stepX
    y += stepY
    
    # textSize(32)
    # text("ABDURAHMAN", 50 + x, 100 + y, -30)
    
    img = loadImage("dot.png")
    image(img, 50 + x, 50 + y, 100, 100)

    #circle(100 + x, 100 + y, 100)
    if y > height -150 or y < -50:
        #fill(int(random(0, 255)), int(random(0, 255)), int(random(0, 255)))
        stepY = -stepY
    if x > width -150 or x < -50:
        #fill(int(random(0, 255)), int(random(0, 255)), int(random(0, 255)))
        stepX = -stepX
