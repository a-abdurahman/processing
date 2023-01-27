def setup():
    size(700, 600)
    background(0, 50, 50)
    
    
def draw():    
    noStroke()
    if mouseButton == LEFT:
        fill(int(random(0, 255)),(random(0, 255)),(random(0, 255)))
        circle(mouseX, mouseY, 20)
    if mouseButton == RIGHT:
        background(0, 50, 50)
 
    fill(0, 20, 10)
    rect(0, 0, 700, 100)
    rect(000, 500, 700, 100)
    rect(0, 100, 100, 500)
    rect(600, 100, 100, 500)
    
    fill(255)
    textSize(15)
    text("X: " + str(mouseX), 20, 20)
    text("Y: " + str(mouseY), 20, 40)
    
